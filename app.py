import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample training data (replace this with your real data/model if you want)
X = np.array([[1400, 3], [1600, 3], [1700, 3], [1875, 4], [1100, 2]])
y = np.array([245000, 312000, 279000, 308000, 199000])

# Train model
model = LinearRegression()
model.fit(X, y)

# Streamlit app
st.title("🏡 House Price Predictor")
st.write("Enter the details below to predict the price of a house.")

# User inputs
size = st.number_input("Enter the size of the house (sqft):", min_value=500, max_value=10000, step=50)
bedrooms = st.number_input("Number of bedrooms:", min_value=1, max_value=10, step=1)

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[size, bedrooms]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ${int(prediction):,}")
