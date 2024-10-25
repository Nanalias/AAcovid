import streamlit as st
st.header('Data Description on Covid-19 Data')

import pandas as pd

#st.write(df.head())
st.caption("The first 5 rows of banking dataset were shown below")
df = pd.read_csv('dataset.csv')
st.dataframe(df.head())

st.subheader("Covid-19 Dataset Information")
st.text(f"Dimension of dataset: {df.ndim}") # show dimension
st.text(f"Shape of dataset: {df.shape}")  # Show rows and columns count
st.text(f"List of variables name in dataset: {df.columns}") # Show variables 
st.text(f"Range index of dataset: {df.index}")# Show range index 

import io
# Create a buffer to capture the output of df.info()
buffer = io.StringIO()
df.info(buf=buffer)
info = buffer.getvalue()

# Display df.info() output in Streamlit
st.subheader("DataFrame Information - Data Type, Rows, Columns")
st.text(info)

# Check for missing data
st.subheader("Missing Data Summary")
missing_data = df.isnull().sum()
missing_data = missing_data[missing_data > 0]  # Filter to show only columns with missing data

# Display missing data summary
if not missing_data.empty:
    st.write("The following columns have missing values:")
    st.write(missing_data)
else:
    st.write("No missing values in the dataset.")