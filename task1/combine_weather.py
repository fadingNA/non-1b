import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


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


# Check for missing values
missing_values = combined_df.isnull().sum()
print(f"Missing values:\n{missing_values}\n")

# Check DataTypes
print(f"Data Types:\n{combined_df.dtypes}\n")

# Check for duplicates
duplicates = combined_df.duplicated().sum()
print(f"Duplicates:\n{duplicates}\n")

# Description of the data
description_data = combined_df.describe()
print(f"Description of the data:\n{description_data}\n")



print(f'Number of rows before removing duplicates: {combined_df.shape}')

combined_df['LOCAL_DATE'] = pd.to_datetime(combined_df['LOCAL_DATE'])
combined_df['UTC_DATE'] = pd.to_datetime(combined_df['UTC_DATE'])


"""
plt.figure(figsize=(10, 6))
sns.histplot(data=combined_df, x='TEMP', bins=30, kde=True, multiple='stack')
plt.title('Distribution of Temperature')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.show()

# Plot the distribution of the temperature
# Mostly normal distribution with a few outliers 0 to -5 temp

plt.figure(figsize=(10, 6))
sns.boxplot(data=combined_df, x='WIND_SPEED')
plt.title('Distribution of Wind Speed')
plt.xlabel('Wind Speed (km/h)')
plt.show()

"""

# Scatter plot to check the relationship between temperature and humidity
plt.figure(figsize=(10, 6))
sns.scatterplot(data=combined_df, x='TEMP', y='RELATIVE_HUMIDITY')
plt.title('Temperature vs Relative Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Relative Humidity (%)')
plt.show()

# Group data by 'STATION_NAME' to see the average wind speed at each station
average_wind_speed_per_station = combined_df.groupby('STATION_NAME')['WIND_SPEED'].mean().sort_values(ascending=False)
print(average_wind_speed_per_station)

