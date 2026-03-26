import streamlit as st
import pandas as pd
from model import load_and_process_data, compute_similarity
# Load and process data
data, scaled_features = load_and_process_data()
similarity_matrix = compute_similarity(scaled_features)
# Recommendation function
def recommend_products(product_name, top_n=3):
    if product_name not in data['Product'].values:
        return []
    index = data[data['Product'] == product_name].index[0]
    similarity_scores = list(enumerate(similarity_matrix[index]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    return data.iloc[recommended_indices]
# Streamlit UI
st.title("Product Recommendation System")
st.write("Select a product to get similar product recommendations.")
# Dropdown for product selection
product_list = data['Product'].values
selected_product = st.selectbox("Choose a product", product_list)
# Number of recommendations
num_recommendations = st.slider("Number of recommendations", 1, 5, 3)
# Button to generate recommendations
if st.button("Get Recommendations"):
    results = recommend_products(selected_product, num_recommendations)
    if len(results) == 0:
        st.write("Product not found.")
    else:
        st.subheader("Recommended Products:")
        st.dataframe(results[['Product', 'Category', 'Price', 'Rating']])
