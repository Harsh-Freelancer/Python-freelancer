const products = [
    {
        id: 1,
        name: "Luxury Rose Soap",
        category: "Bath & Body",
        price: 99,
        rating: 4.5,
        image: "https://images.unsplash.com/photo-1583947581927-860c9f8e8b8d?w=300&h=200&fit=crop",
        alt: "soap bar"
    },
    {
        id: 2,
        name: "Spicy Potato Chips",
        category: "Snacks",
        price: 40,
        rating: 4.2,
        image: "https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=300&h=200&fit=crop",
        alt: "chips"
    },
    {
        id: 3,
        name: "Chill Cola Coldrink",
        category: "Beverages",
        price: 55,
        rating: 4.8,
        image: "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=300&h=200&fit=crop",
        alt: "cold drink"
    },
    {
        id: 4,
        name: "Aloe Vera Shampoo",
        category: "Hair Care",
        price: 199,
        rating: 4.3,
        image: "https://images.unsplash.com/photo-1597773150796-e5c14ebecbf5?w=300&h=200&fit=crop",
        alt: "shampoo"
    },
    {
        id: 5,
        name: "Classic Butter Biscuits",
        category: "Snacks",
        price: 35,
        rating: 4.6,
        image: "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?w=300&h=200&fit=crop",
        alt: "biscuits"
    },
    {
        id: 6,
        name: "Energy Burst Drink",
        category: "Beverages",
        price: 110,
        rating: 4.4,
        image: "https://images.unsplash.com/photo-1615238346069-3d6c5b2e24a7?w=300&h=200&fit=crop",
        alt: "energy drink"
    },
    {
        id: 7,
        name: "Coconut Coldrink",
        category: "Beverages",
        price: 60,
        rating: 4.1,
        image: "https://images.unsplash.com/photo-1581004147493-0e9e6fb6d562?w=300&h=200&fit=crop",
        alt: "coconut drink"
    },
    {
        id: 8,
        name: "Lemon Hand Wash Soap",
        category: "Bath & Body",
        price: 89,
        rating: 4.7,
        image: "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=300&h=200&fit=crop",
        alt: "hand wash"
    }
];

let cartCount = 0;

function renderProducts() {
    const container = document.getElementById('products-container');
    container.innerHTML = '';
    products.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
            <img class="product-img" src="${product.image}" alt="${product.alt}" loading="lazy">
            <div class="product-info">
                <div class="product-title">${product.name}</div>
                <div class="product-category">${product.category}</div>
                <div class="product-price">₹${product.price}</div>
                <div class="rating">${'★'.repeat(Math.floor(product.rating))}${product.rating % 1 ? '½' : ''} (${product.rating})</div>
                <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
            </div>
        `;
        container.appendChild(card);
    });

    document.querySelectorAll('.add-to-cart').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const id = parseInt(btn.dataset.id);
            const product = products.find(p => p.id === id);
            cartCount++;
            document.getElementById('cart-count').innerText = cartCount;
            alert(`🛒 Added: ${product.name} to cart`);
        });
    });
}

// Search functionality
function setupSearch() {
    const searchInput = document.querySelector('.search-bar input');
    const searchBtn = document.querySelector('.search-bar button');
    
    function filterProducts() {
        const query = searchInput.value.toLowerCase();
        const cards = document.querySelectorAll('.product-card');
        cards.forEach((card, index) => {
            const title = card.querySelector('.product-title').innerText.toLowerCase();
            if (title.includes(query)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }
    
    searchBtn.addEventListener('click', filterProducts);
    searchInput.addEventListener('keyup', (e) => {
        if (e.key === 'Enter') filterProducts();
    });
}

renderProducts();
setupSearch();