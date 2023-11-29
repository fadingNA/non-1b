import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('data/historical_storms.csv')


st.title('Historical Data Storms Last 5 years')
st.write(data)


st.title('Climate Daily Basis Data')
data_climate = pd.read_csv('data/Toronto_Climate.csv')
st.write(data_climate)


start_year, end_year = st.slider("Select the year range", 2015, 2020, (2018, 2020))
filtered_data = data_climate[(data_climate['LOCAL_YEAR'] >= start_year) & (data_climate['LOCAL_YEAR'] <= end_year)]

# Display filtered data
st.write(filtered_data)

