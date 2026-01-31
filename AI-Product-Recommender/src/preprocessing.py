import pandas as pd

def load_data():
    df = pd.read_csv('data/products.csv')
    df['combined_features'] = df['product_name'] + " " + df['category'] + " " + df['description']
    return df