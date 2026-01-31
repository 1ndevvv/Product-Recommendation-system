import streamlit as st
import pandas as pd
import sys
import os

# --- 1. Setup Path to find the 'src' folder ---
# This line tells Streamlit: "Look for code in the main folder too"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import load_data
from src.models import build_content_model, build_collaborative_model
from src.recommender import hybrid_recommend

# --- 2. Page Config ---
st.set_page_config(page_title="Hybrid AI Recommender", page_icon="🛍️")

# --- 3. Load Data & Models (Cached for Speed) ---
@st.cache_resource
def load_engine():
    df = load_data()
    tfidf, vectorizer = build_content_model(df)
    svd_data = build_collaborative_model(df)
    return df, tfidf, svd_data

try:
    df, tfidf_matrix, svd_data = load_engine()
    status_text = "✅ System Online"
except Exception as e:
    st.error(f"Failed to load AI Engine: {e}")
    status_text = "🔴 System Offline"

# --- 4. UI Layout ---
st.title("🛍️ Hybrid AI Product Recommender")
st.markdown(f"**Status:** {status_text}")
st.write("Combines **Content Filtering** (Item Similarity) + **Collaborative Filtering** (User Preferences).")

# Sidebar Controls
st.sidebar.header("User Settings")
user_id = st.sidebar.number_input("User ID", min_value=1, max_value=50, value=5)
selected_product = st.sidebar.selectbox("Select a Product you are viewing:", df['product_name'].unique())

# --- 5. Recommendation Logic ---
if st.button("Get Personalized Recommendations"):
    with st.spinner("Analyzing user history & product features..."):
        # DIRECT CALL (No more API/Localhost issues!)
        recommendations = hybrid_recommend(user_id, selected_product, df, svd_data, tfidf_matrix)
        
        if recommendations:
            st.success(f"Top 5 Picks for User {user_id}:")
            for rec in recommendations:
                st.info(f"**{rec[0]}** (Confidence: {rec[1]:.2f}) - *{rec[2]}*")
        else:
            st.warning("No recommendations found.")

# --- 6. Debug Info (Optional) ---
with st.expander("See How It Works"):
    st.write("This app uses TF-IDF to find similar items and SVD (Singular Value Decomposition) to predict what you will like based on your 'User ID' history.")