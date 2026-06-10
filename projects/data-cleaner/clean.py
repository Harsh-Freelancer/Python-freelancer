import pandas as pd
import re

def clean_csv_file(input_file, output_file):
    df = pd.read_csv(input_file)
    
    print(f"Original rows: {len(df)}")
    
    df = df.drop_duplicates()
    print(f"After removing duplicates: {len(df)}")
    
    df = df.fillna("N/A")
    
    if 'phone' in df.columns:
        df['phone'] = df['phone'].astype(str).apply(lambda x: re.sub(r'\D', '', x)[-10:] if len(re.sub(r'\D', '', x)) >= 10 else 'Invalid')
    
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')
        df['date'] = df['date'].fillna('Invalid Date')
    
    string_columns = df.select_dtypes(include=['object']).columns
    for col in string_columns:
        df[col] = df[col].astype(str).str.strip()
    
    df.to_csv(output_file, index=False)
    print(f"Saved: {output_file}")
    print(f"Final rows: {len(df)}")
    return df

clean_csv_file("sample_data.csv", "cleaned_data.csv")