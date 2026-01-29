import streamlit as st 
import plotly.express as px
import pandas as pd
import joblib

countries_list = joblib.load('countries_list.plk')
unique_actors = joblib.load('unique_actors.plk') 
geners = joblib.load('gener_list.plk')

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

gener = st.sidebar.multiselect(
    'Select Gener',
    options=geners
)

year = st.sidebar.slider('Select Year',df['year'].min(),df['year'].max())

col1, col2 = st.columns([0.3,0.7])

with col1:
    fig = px.bar(df.head(20),x='revenue',y='title')
    st.plotly_chart(fig)
    
with col2: 
    fig = px.line(df.head(20),y='date_added',x='popularity')
    st.plotly_chart(fig) 

# px.histogram(data=df.head(20),x='revenue',y='title')
st.write(df)
