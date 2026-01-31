from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import pandas as pd

# 1. Content-Based Model
def build_content_model(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    matrix = vectorizer.fit_transform(df['combined_features'])
    return matrix, vectorizer

# 2. Collaborative Model (Using SVD from Scikit-Learn instead of Surprise)
def build_collaborative_model(df):
    pivot = df.pivot_table(index='user_id', columns='product_id', values='rating').fillna(0)
    svd = TruncatedSVD(n_components=5, random_state=42)
    svd.fit(pivot)
    return svd, pivot