import streamlit as st
import pandas as pd

# Ensure page configuration is the very first Streamlit command
st.set_page_config(page_title="House Price Prediction Dataset Overview", page_icon="🏠")

# Custom CSS for controlling width and padding
st.markdown(
    """
    <style>
    .main-content {
        max-width: 1000px;  /* Limit the width of the content */
        margin: 0 auto;     /* Center the content */
        padding: 20px;      /* Add padding on the left and right */
    }
    </style>
    """, unsafe_allow_html=True
)

# Start the main container with padding and max-width applied
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Title
st.title("🏠 House Price Prediction")

# Display the image
st.image("/workspaces/DataScience_tutorial/Project/Image/houseprediction.png", caption="House Price Prediction", use_column_width=True)

# Add space after the image
st.write("")

# Introduction
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

# Close the main-content div
st.markdown('</div>', unsafe_allow_html=True)


# Import and display dataset section
st.header("Module 1: Importing Data Sets")

# File path to the dataset
file_path = '/workspaces/DataScience_tutorial/Project/Datasets/kc_house_data.csv'

# Load the dataset
try:
    df = pd.read_csv(file_path)
    
    # Dropdown selection for displaying the dataframe
    view_data = st.selectbox("Would you like to view the dataset?", ("No", "Yes"))
    
    # Conditionally display the dataframe
    if view_data == "Yes":
        st.write("### First 5 Rows of the Dataset")
        st.dataframe(df.head())
except FileNotFoundError:
    st.error("Dataset not found. Please check the file path and ensure the dataset is available.")

# Close the main-content div
st.markdown('</div>', unsafe_allow_html=True)