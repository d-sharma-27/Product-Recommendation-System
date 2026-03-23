import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

def load_and_process_data(file_path="dataset.csv"):
    # Load dataset
    data = pd.read_csv(file_path)

    # Encode category without removing original values
    data['Category_Code'] = data['Category'].astype('category').cat.codes

    # Select features
    features = data[['Category_Code', 'Price', 'Rating']]

    # Normalize features
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(features)

    return data, scaled_features

def compute_similarity(scaled_features):
    # Compute cosine similarity matrix
    similarity_matrix = cosine_similarity(scaled_features)
    return similarity_matrix
