import streamlit as st 
import plotly.express as px
import pandas as pd
import joblib

countries_list = joblib.load('countries_list.plk')
unique_actors = joblib.load('unique_actors.plk') 

df = pd.read_csv('cleaned.csv')



country = st.sidebar.multiselect(
    'Select the country',
    options=countries_list
)

director = st.sidebar.multiselect(
    'Select Director',
    options=df['director'].unique()
)

actors = st.sidebar.multiselect(
    'Select Actors',
    options=unique_actors
)

year = st.sidebar.slider('Select Year',df['year'].min(),df['year'].max())

st.write(df)