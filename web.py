import streamlit as st 
import plotly.express as px
import pandas as pd
import joblib

unique_actors = joblib.load('unique_actors.plk') 
gener_df = joblib.load('gener_df.plk')
country_df = joblib.load('country_df.plk')

df = pd.read_csv('cleaned.csv')

date_df = df.copy()
date_df['date_added'] = pd.to_datetime(df['date_added']).dt.strftime('%Y-%m')  #('%Y-%Q%q')


st.title('HOLLYWOOD MOVIES ANALYSIS FROM 2K10 TO 2025')
st.set_page_config(page_title='Netflix Data Analysis',layout='wide',initial_sidebar_state='expanded')

letterboxd_palette = [
    '#FF8000', '#00E054', '#40BCF4', '#EE3424', '#99AABB', 
    '#202830', '#00B020', '#BB6600', '#CCDDEE', '#445566'
]

countries = st.sidebar.multiselect(
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

start_year = st.sidebar.date_input('Select Year Start Year',min_value=df['date_added'].min(),max_value=df['date_added'].max(),)
end_year = st.sidebar.date_input('Select Year End Year',min_value=df['date_added'].min(),max_value=df['date_added'].max())

btn = st.sidebar.button('Analyze', type= 'primary')

if btn:

    df = df.query(
        "country in countries"
    )

    gener_df = gener_df.query(
        "country in countries "
    )

    date_df = date_df.query(
        "country in countries"
    )

    country_df = country_df.query(
        "country in countries"
    )


    tab1,tab2,tab3 = st.tabs(['Revenue','Popularity','Rating'])

    with tab1 :
        col1, col2 = st.columns(2)
        with col1:
            
            new_df = country_df.groupby('country')['revenue'].mean().reset_index()
            fig = px.choropleth(new_df,locations='country',
                                locationmode='country names',
                                color='revenue',
                                hover_data=['country','revenue'],
                                color_continuous_scale=letterboxd_palette)
            
            st.plotly_chart(fig,key='revenue map')
            
        with col2: 
            fig_scatter = px.scatter(df,x='budget',y='revenue',
                                    hover_data=['title','budget','revenue'],
                                    color_discrete_sequence= letterboxd_palette)
            st.plotly_chart(fig_scatter) 
    
            
        new_df = date_df.groupby('date_added')[['revenue','budget']].sum().reset_index()
        new_df = new_df.sort_values(by='date_added',ascending=True)
            
        fig = px.line(new_df, x = 'date_added', 
                                y= ['revenue','budget'],
                                color_discrete_sequence=letterboxd_palette,
                                line_shape= 'linear',
                        )
            
        st.plotly_chart(fig)

    
        col4,col5 = st.columns(2)  

        with col4:
            new_df = df.nlargest(20,'revenue').reset_index()
            
            fig = px.bar(new_df,y='title',x=['revenue','budget'],orientation='h',
                        color_discrete_sequence=letterboxd_palette)
            st.plotly_chart(fig)
        
        with col5: 
            
            fig = px.pie(gener_df,names='genres',values='revenue',
                        color_discrete_sequence=letterboxd_palette)
            st.plotly_chart(fig)
            
            
    with tab2:    
            pass



