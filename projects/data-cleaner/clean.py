import pandas as pd
import re

def clean_csv_file(input_file, output_file):
    df = pd.read_csv(input_file)
    
    print(f"Original rows: {len(df)}")
    
    df = df.drop_duplicates()
    print(f"After removing duplicates: {len(df)}")
    
    df = df.fillna("N/A")
    
    if 'phone' in df.columns:
        df['phone'] = df['phone'].apply(lambda x: re.sub(r'\D', '', str(x))[:10])
    
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    string_columns = df.select_dtypes(include=['object']).columns
    for col in string_columns:
        df[col] = df[col].str.strip()
    
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned file saved: {output_file}")
    print(f"Final rows: {len(df)}")
    
    return df

if __name__ == "__main__":
    clean_csv_file("messy_data.csv", "cleaned_data.csv")