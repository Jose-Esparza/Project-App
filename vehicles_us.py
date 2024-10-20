import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header('Vehicle Information')
st.write('Filter the data below to see vehicles by category.')

df = pd.read_csv('vehicles_us.csv')

category = df['type'].unique()

selected_type = st.selectbox('Select a Category',category)



min_price, max_price = int(df['price'].min()), int(df['price'].max())

price_range = st.slider('Price range', value=(min_price, max_price) ,min_value = min_price, max_value = max_price)


actual_price = list(range(price_range[0], price_range[1]+1))

df_filtered = df[(df.type == selected_type) & (df.price.isin(list(actual_price)))]

check = st.checkbox('Remove vehicles with no odometer information')

if check:
    df_filtered = df_filtered.loc[df_filtered['odometer'].notna()]

df_filtered



st.header('Price Analysis')
st.write('Analysis of price difference between engine fuel types and transmissions.')

list_for_hist = ['fuel','transmission']

selected_thing = st.selectbox('Split for price distribution', list_for_hist)

fig1 = px.histogram(df, x = 'price', color = selected_thing)
fig1.update_layout(title = '<b> Split price by {}</b>'.format(selected_thing))

st.plotly_chart(fig1)

def age_category(x):
    if x<25: return '<25'
    elif x>=25 and x<50: return '25-49'
    elif x>= 50 and x<75: return '50-74'
    elif x>= 75 and x<100: return '75-99'
    elif x>= 100 and x<117: return '100-116'
    else: return 'unknown'

df['age'] = 2024 - df['model_year']

df['age_category'] = df['age'].apply(age_category)

list_for_scatter = ['odometer','cylinders']

choice_for_scatter = st.selectbox('Price dependency on', list_for_scatter)

fig2 = px.scatter(df, x='price', y=choice_for_scatter, color = 'age_category',hover_data=['model_year'])
fig2.update_layout(title='<b> Price vs {}</b>'.format(choice_for_scatter))
st.plotly_chart(fig2) 
