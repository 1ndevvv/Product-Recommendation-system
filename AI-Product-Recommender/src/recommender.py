import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def hybrid_recommend(user_id, product_name, df, svd_data, tfidf_matrix):
    # 1. Content-Based
    try:
        idx = df[df['product_name'] == product_name].index[0]
        sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix)[0]
        top_indices = sim_scores.argsort()[-11:-1][::-1]
        candidates = df.iloc[top_indices].drop_duplicates('product_id')
    except IndexError:
        return []

    # 2. Collaborative Filtering
    svd_model, pivot = svd_data
    predictions = []
    
    if user_id in pivot.index:
        user_idx = pivot.index.get_loc(user_id)
        user_preds = svd_model.inverse_transform(svd_model.transform(pivot))[user_idx]
        
        for _, row in candidates.iterrows():
            if row['product_id'] in pivot.columns:
                col_idx = pivot.columns.get_loc(row['product_id'])
                score = user_preds[col_idx]
            else:
                score = row['rating']
            predictions.append((row['product_name'], score, row['category']))
    else:
        for _, row in candidates.iterrows():
            predictions.append((row['product_name'], row['rating'], row['category']))
            
    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:5]