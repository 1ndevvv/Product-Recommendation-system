from fastapi import FastAPI
from src.preprocessing import load_data
from src.models import build_content_model, build_collaborative_model
from src.recommender import hybrid_recommend

app = FastAPI()

# Initialize System
df = load_data()
tfidf_matrix, vectorizer = build_content_model(df)
svd_model = build_collaborative_model(df)

@app.get("/")
def home():
    return {"status": "Hybrid Recommender Online"}

@app.get("/recommend")
def recommend(user_id: int, product_name: str):
    recs = hybrid_recommend(user_id, product_name, df, svd_model, tfidf_matrix)
    return {"user_id": user_id, "based_on": product_name, "recommendations": recs}