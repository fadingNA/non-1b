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

# Define a function to clean individual DataFrames
def clean_dataframe(file_path, relevant_columns):
    df = pd.read_csv(file_path, low_memory=False)
    df = df[relevant_columns]
    
    # Convert columns that should be numeric
    numeric_columns = ['WINDCHILL', 'HUMIDEX', 'VISIBILITY', 'WIND_SPEED', 'PRECIP_AMOUNT']
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    
    return df

# List of your CSV files
csv_files = [
    './data/weather_data2016.csv',
    './data/weather_data2017.csv',
    './data/weather_data2018.csv',
    './data/weather_data2019.csv',
    './data/weather_data2020.csv',
    './data/weather_data2021.csv',
    './data/weather_data2022.csv',
    './data/weather_data2023.csv'
]

# Load the first CSV file and clean it
combined_df = clean_dataframe(csv_files[0], relevant_columns)

# Iterate over the rest of the files, clean, and combine them into combined_df
for file_path in csv_files[1:]:
    cleaned_df = clean_dataframe(file_path, relevant_columns)
    combined_df = pd.concat([combined_df, cleaned_df], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('./data/combined_weather_data.csv', index=False)

# Print DataFrame information and head for verification
print(combined_df.info(), combined_df.head())
