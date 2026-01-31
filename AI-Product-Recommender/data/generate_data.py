import pandas as pd
import random

# 1. Define Products
products = [
    {'product_id': 101, 'product_name': 'Sony WH-1000XM5', 'category': 'Electronics', 'description': 'Noise cancelling headphones 30hr battery'},
    {'product_id': 102, 'product_name': 'MacBook Air M2', 'category': 'Electronics', 'description': 'Apple laptop M2 chip lightweight'},
    {'product_id': 103, 'product_name': 'Nike Air Max', 'category': 'Fashion', 'description': 'Running shoes air cushioning comfort'},
    {'product_id': 104, 'product_name': 'PlayStation 5', 'category': 'Electronics', 'description': 'Next gen gaming console 4k graphics'},
    {'product_id': 105, 'product_name': 'Dell XPS 13', 'category': 'Electronics', 'description': 'Windows laptop infinity edge display'},
    {'product_id': 106, 'product_name': 'Adidas Ultraboost', 'category': 'Fashion', 'description': 'High performance running shoes boost'},
    {'product_id': 107, 'product_name': 'iPhone 14 Pro', 'category': 'Electronics', 'description': 'Apple phone dynamic island camera'},
    {'product_id': 108, 'product_name': 'Levi\'s 501 Jeans', 'category': 'Fashion', 'description': 'Classic original fit denim jeans blue'},
]

# 2. Simulate User Behavior (Hybrid Logic Needs This!)
data = []
print("Generating synthetic user data...")
for _ in range(500): # 500 interactions
    user = random.randint(1, 20) # 20 Users
    prod = random.choice(products)
    # Simulate: Users stick to categories (Bias)
    rating = random.randint(3, 5) if user % 2 == 0 and prod['category'] == 'Electronics' else random.randint(1, 4)
    
    row = prod.copy()
    row['user_id'] = user
    row['rating'] = rating
    data.append(row)

# 3. Save
df = pd.DataFrame(data)
df.to_csv('data/products.csv', index=False)
print("✅ Success! data/products.csv created.")
