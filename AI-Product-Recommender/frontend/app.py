import streamlit as st
import requests

st.title("🧠 Hybrid AI Product Recommender")
st.markdown("Combines **Content Filtering** (Item Similarity) + **Collaborative Filtering** (User Preference).")

col1, col2 = st.columns(2)
with col1:
    user_id = st.number_input("User ID (1-20)", min_value=1, max_value=20, value=5)
with col2:
    product_name = st.selectbox("Product You Liked:", [
        "Sony WH-1000XM5", "MacBook Air M2", "Nike Air Max", "PlayStation 5"
    ])

if st.button("Get Personalized Recommendations"):
    try:
        res = requests.get(f"http://127.0.0.1:8000/recommend?user_id={user_id}&product_name={product_name}")
        data = res.json()
        
        st.subheader("Top Picks For You:")
        for item in data['recommendations']:
            st.success(f"**{item[0]}** ({item[2]}) - Predicted Rating: {item[1]:.1f}/5 ⭐")
    except:
        st.error("Backend is offline. Run 'uvicorn api.main:app' first.")