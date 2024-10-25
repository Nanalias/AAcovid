import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader('Data Dictionary')

data_dict=pd.read_excel("data_dictionary.xlsx")
st.dataframe(data_dict)

st.subheader('Data Exploration on Covid-19 Data')
st.caption('To understand the quality of the dataset')


df = pd.read_csv('dataset.csv')
# Create histograms of the dataset
fig, ax = plt.subplots(figsize=(20, 20))
df.hist(ax=ax)
st.pyplot(fig) 