import streamlit as st 
import plotly.express as px
import pandas as pd
import joblib

unique_actors = joblib.load('unique_actors.plk') 
gener_df = joblib.load('gener_df.plk')
country_df = joblib.load('country_df.plk')

df = pd.read_csv('cleaned.csv')


country = st.sidebar.multiselect(
    'Select the country',
    options=country_df['country'].unique()
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
    options=gener_df['genres'].unique()
)

year = st.sidebar.date_input('Select Year Start Year',min_value=df['date_added'].min(),max_value=df['date_added'].max(),)
year = st.sidebar.date_input('Select Year End Year',min_value=df['date_added'].min(),max_value=df['date_added'].max())

st.title('NETFLIX MOVIE ANALYSIS')

tab1,tab2,tab3 = st.tabs(['Revenue','Popularity','Rating'])

with tab1 :
    col1, col2,col3 = st.columns(3)
    with col1:
        fig = px.bar(df.head(20),y='revenue',x='title')
        st.plotly_chart(fig)
        
    with col2: 
        fig = px.line(df,x='year',y='revenue')
        st.plotly_chart(fig) 


    with col3:
        fig = px.scatter(df, x = 'budget', y='revenue',hover_data='title')
        st.plotly_chart(fig)
      
    col4,col5,col6 = st.columns(3)  
    
    with col4:
        new_df = country_df.groupby('country')['revenue'].sum().reset_index()
        
        fig = px.bar(new_df.sort_values(by='revenue').head(20),y='country',x='revenue')
        st.plotly_chart(fig)

   

    with col5:
        new_df = gener_df.groupby('genres')['rating'].sum().reset_index()
        # st.write(new_df)
        
        fig = px.pie(new_df,names='genres',values='rating')
        st.plotly_chart(fig)
    
with tab2:    
    with col6: 
        fig = px.line(country_df,x='year',y='popularity',labels='country')
        st.plotly_chart(fig)
        


# px.histogram(data=df.head(20),x='revenue',y='title')
st.write(df)
