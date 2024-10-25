import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader('Data Preprocessing on COVID-19 Data')
st.caption('The following processes were executed in the background:')

# Data Mapping Process
st.caption('1) Data Mapping')

# Load the dataset
df = pd.read_csv('dataset.csv')

# Map categorical variables to meaningful labels
df["SEX"] = df["SEX"].map({1: "FEMALE", 2: "MALE", 99: "UNKNOWN"})
df["HOSPITALIZED"] = df["HOSPITALIZED"].map({1: "NO", 2: "YES", 99: "UNKNOWN"})
df["INTUBATED"] = df["INTUBATED"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["PNEUMONIA"] = df["PNEUMONIA"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["PREGNANCY"] = df["PREGNANCY"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["OTHER_DISEASE"] = df["OTHER_DISEASE"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["CARDIOVASCULAR"] = df["CARDIOVASCULAR"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["OBESITY"] = df["OBESITY"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["CHRONIC_KIDNEY"] = df["CHRONIC_KIDNEY"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["TOBACCO"] = df["TOBACCO"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["SPEAKS_NATIVE_LANGUAGE"] = df["SPEAKS_NATIVE_LANGUAGE"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["DIABETES"] = df["DIABETES"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["COPD"] = df["COPD"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["ASTHMA"] = df["ASTHMA"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["INMUSUPR"] = df["INMUSUPR"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["HYPERTENSION"] = df["HYPERTENSION"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["ANOTHER CASE"] = df["ANOTHER CASE"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["MIGRANT"] = df["MIGRANT"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["ICU"] = df["ICU"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["OUTCOME"] = df["OUTCOME"].map({1: "POSITIVE", 2: "NEGATIVE", 3: "PENDING"})
df["NATIONALITY"] = df["NATIONALITY"].map({1: "MEXICAN", 2: "FOREIGN", 99: "UNKNOWN"})

# Create a new variable based on existing variables (example)
# You can customize this part based on your analysis needs
# Example: df['NEW_VARIABLE'] = df['HOSPITALIZED'] + df['INTUBATED'] # (Just an example, modify as needed)


st.caption('2) Create New Variable = AGE_GROUP')

# Create age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

# Create the AGE_GROUP variable
df['AGE_GROUP'] = pd.cut(x=df['AGE'], bins=age_bins, labels=age_labels, right=False)

st.caption('2) Create New Variable = DECEASED')
# Create DECEASED variable based on date_of_death
df['DECEASED'] = df['DATE_OF_DEATH'].notna()  # True if date_of_death is not null


st.subheader('Original Data vs Cleaned Data')

st.markdown("Original Data")
df_ori=pd.read_csv("dataset.csv")
st.dataframe(df_ori.head())

st.markdown("Cleaned Data")
st.dataframe(df.head())