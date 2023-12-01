import streamlit as st
import pandas as pd
import numpy as np


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


import ast

# Function to safely parse a string representation of a dictionary
def safe_parse_dict(column):
    return column.apply(ast.literal_eval)

weather_df = pd.read_csv('weathergc.csv')

# Applying the function to 'geometry' and 'properties' columns
weather_df['geometry'] = safe_parse_dict(weather_df['geometry'])
weather_df['properties'] = safe_parse_dict(weather_df['properties'])

# Expanding the nested dictionaries into separate columns
geometry_df = weather_df['geometry'].apply(pd.Series)
properties_df = weather_df['properties'].apply(pd.Series)

# Merging the expanded columns back into the main DataFrame
weather_df_expanded = pd.concat([weather_df.drop(['geometry', 'properties'], axis=1), geometry_df, properties_df], axis=1)

# Displaying the first few rows of the expanded DataFrame
st.title('Weather Data')
st.write(weather_df_expanded)


