import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("dataset.csv")

# Encode category without losing original values
data['Category_Code'] = data['Category'].astype('category').cat.codes

# Select features
features = data[['Category_Code', 'Price', 'Rating']]

# Normalize features
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(features)

# Compute similarity matrix
similarity_matrix = cosine_similarity(scaled_features)

# Recommendation function
def recommend_products(product_name, top_n=3):
    if product_name not in data['Product'].values:
        print("Product not found in dataset.")
        return

    index = data[data['Product'] == product_name].index[0]
    similarity_scores = list(enumerate(similarity_matrix[index]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommended_indices = [i[0] for i in sorted_scores[1:top_n+1]]

    print(f"\nTop {top_n} recommendations for '{product_name}':\n")

    for i in recommended_indices:
        print(f"Product: {data.iloc[i]['Product']}, "
              f"Category: {data.iloc[i]['Category']}, "
              f"Price: {data.iloc[i]['Price']}, "
              f"Rating: {data.iloc[i]['Rating']}")

# User input
if __name__ == "__main__":
    product_input = input("Enter a product name: ")
    recommend_products(product_input)
