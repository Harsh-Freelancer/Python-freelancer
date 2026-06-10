import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'
}

def get_amazon_product(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    try:
        title = soup.find('span', {'id': 'productTitle'}).get_text().strip()
    except:
        title = 'N/A'
    
    try:
        price = soup.find('span', {'class': 'a-price-whole'}).get_text().strip()
    except:
        price = 'N/A'
    
    try:
        rating = soup.find('span', {'class': 'a-icon-alt'}).get_text().strip()
    except:
        rating = 'N/A'
    
    try:
        reviews = soup.find('span', {'id': 'acrCustomerReviewText'}).get_text().strip()
    except:
        reviews = 'N/A'
    
    return {
        'title': title,
        'price': price,
        'rating': rating,
        'reviews': reviews,
        'url': url
    }

def search_amazon(query, max_results=5):
    search_url = f'https://www.amazon.in/s?k={query.replace(" ", "+")}'
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    results = soup.find_all('div', {'data-component-type': 's-search-result'})[:max_results]
    
    for result in results:
        try:
            link = 'https://www.amazon.in' + result.find('a', {'class': 'a-link-normal'})['href']
            products.append(get_amazon_product(link))
            time.sleep(random.uniform(1, 3))
        except:
            continue
    
    return products

if __name__ == '__main__':
    search_term = input("Enter product to search: ")
    print(f"Searching for {search_term}...")
    
    data = search_amazon(search_term, 5)
    
    df = pd.DataFrame(data)
    df.to_csv('amazon_products.csv', index=False)
    
    print(f"\n✅ Found {len(data)} products")
    print("✅ Saved to amazon_products.csv")
    
    for product in data:
        print(f"\n📦 {product['title'][:50]}...")
        print(f"💰 Price: ₹{product['price']}")
        print(f"⭐ Rating: {product['rating']}")