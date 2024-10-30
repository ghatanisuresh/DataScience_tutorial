import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="House Price Prediction Dataset Overview", page_icon="🏠")

# Title and introduction
st.title("🏠 House Price Prediction Dataset Overview")
st.write("""
This dataset contains house sale prices for **King County**, which includes Seattle. 
It includes homes sold between **May 2014 and May 2015**. The dataset has been slightly modified.
""")

# Create a dataframe with dataset details
data = {
    "Variable": [
        "id", "date", "price", "bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors",
        "waterfront", "view", "condition", "grade", "sqft_above", "sqft_basement", "yr_built",
        "yr_renovated", "zipcode", "lat", "long", "sqft_living15", "sqft_lot15"
    ],
    "Description": [
        "🔹 A unique notation for each house",
        "📅 Date the house was sold",
        "💰 Target variable: Price of the house",
        "🛏️ Number of bedrooms",
        "🛁 Number of bathrooms",
        "📐 Square footage of the interior living space",
        "🌳 Square footage of the lot",
        "🏢 Total number of floors (levels) in the house",
        "🌊 Indicates if the house has a waterfront view",
        "👀 Number of times the house has been viewed",
        "🔍 Overall condition of the house",
        "🏆 Overall grade given to the house, based on the King County grading system",
        "📏 Square footage of the house excluding the basement",
        "🕳️ Square footage of the basement",
        "🏗️ Year the house was built",
        "🔧 Year the house was last renovated",
        "📍 Zip code of the house location",
        "🌐 Latitude coordinate",
        "🌐 Longitude coordinate",
        "🛋️ Living room area in 2015 (post-renovations, may or may not affect lot size)",
        "🌲 Lot size area in 2015 (post-renovations)"
    ]
}

# Convert data to a DataFrame for display
df = pd.DataFrame(data)

# Display dataset overview table with styling
st.table(df)

# Add a note section
st.markdown("""
---
✨ **Note**: The dataset is designed to assist in predicting house prices based on a variety of factors, from geographical coordinates to structural attributes.
""")
