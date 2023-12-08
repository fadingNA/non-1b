import pandas as pd
import os


# Set the data directory

# Read in the data
df = pd.read_csv('./data/weather_data2023.csv')

print(df.info(), " | " , df.head())

relevant_columns = [
    'id', 'type', 'longitude', 'latitude', 'PROVINCE_CODE', 'LOCAL_MONTH', 'WINDCHILL',
    'WIND_DIRECTION', 'UTC_MONTH', 'LOCAL_DAY', 'TEMP', 'STATION_NAME', 'UTC_YEAR',
    'HUMIDEX', 'LOCAL_HOUR', 'LOCAL_DATE', 'LOCAL_YEAR', 'VISIBILITY', 'WIND_SPEED', 
    'UTC_DATE', 'DEW_POINT_TEMP', 'RELATIVE_HUMIDITY', 'PRECIP_AMOUNT'
]

df_cleaned = df[relevant_columns].copy()

if all(df_cleaned['id'].astype(str) == df_cleaned['id'].astype(str)):
    df_cleaned.drop('id', axis=1, inplace=True)


for column in df_cleaned.select_dtypes(include=['object']).columns:
    if column in ['WINDCHILL', 'HUMIDEX', 'VISIBILITY', 'WIND_SPEED', 'PRECIP_AMOUNT']:
        df_cleaned[column] = pd.to_numeric(df_cleaned[column], errors='coerce')

# Final check of the cleaned DF

print(df_cleaned.info(), " | " , df_cleaned.head())

def clean_dataframe(file_path, relevant_column):
    df = pd.read_csv(file_path)
    df = df[relevant_column]
    numeric_columns = ['WINDCHILL', 'HUMIDEX', 'VISIBILITY', 'WIND_SPEED', 'PRECIP_AMOUNT']
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

combined_df = df_cleaned.copy()