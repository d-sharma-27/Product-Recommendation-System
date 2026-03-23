Product Recommendation System (Mini AI Project)

Overview
This project is a simple Product Recommendation System developed using fundamental concepts of Artificial Intelligence and Machine Learning. It recommends similar products based on features such as price, rating, and category.
The system uses a content-based filtering approach with similarity measurement to identify and suggest relevant products.

Problem Statement
With a large number of products available online, users often find it difficult to identify items that best match their preferences. This project aims to simplify product discovery by recommending items that are similar to a selected product.

Features
* Recommend similar products based on input
* Uses product attributes such as price and rating
* Lightweight and efficient system
* Beginner-friendly implementation of machine learning concepts
* Optional user interface using Streamlit or command line

Machine Learning Approach
This project uses the following concepts:
* Content-Based Filtering
* Cosine Similarity

Working Principle
1. Product data is loaded from a dataset
2. Important features such as price and rating are selected
3. Similarity between products is calculated
4. Top similar products are recommended to the user

Dataset
The dataset used is a CSV file containing product information.

Example:
```
Product,Category,Price,Rating
Phone A,Electronics,15000,4.2
Phone B,Electronics,20000,4.5
Laptop A,Electronics,50000,4.6
Shirt A,Clothing,800,4.0
Shoes A,Footwear,2000,4.3
```
The dataset can be extended with more products for better recommendations.

Tech Stack
* Python
* Pandas
* Scikit-learn
* Streamlit (optional)
   
 Project Structure
```
Product-Recommendation-System/
│── dataset.csv
│── model.py
│── recommender.py
│── app.py (optional)
│── requirements.txt
│── README.md
│── report.pdf
```

Installation and Setup
1. Clone the repository
```
git clone https://github.com/your-username/Product-Recommendation-System.git
cd Product-Recommendation-System
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Run the project
```
python recommender.py
```

For Streamlit interface:
```
streamlit run app.py
```

Usage
* Enter or select a product name
* The system returns similar product recommendations
* Recommendations are based on feature similarity

Output Example
Input: Phone A
Recommended Products:
* Phone B
* Laptop A
* Watch A

Limitations
* Small dataset may affect recommendation quality
* No user-based personalization
* Limited features used for similarity calculation

Future Improvements
* Implement collaborative filtering
* Expand dataset size
* Improve feature selection
* Develop a more interactive user interface

Learning Outcomes
* Understanding recommendation systems
* Applying similarity-based machine learning techniques
* Working with structured datasets
* Building an end-to-end AI/ML project

