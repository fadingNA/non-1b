import pandas as pd

# Read in the data for the latest year
df = pd.read_csv('./data/weather_data2023.csv')

print(df.info(), " | ", df.head())

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

# Load all CSV files into a list of DataFrames
combined_df_list = [pd.read_csv(file, low_memory=False) for file in csv_files]

# Check for consistent columns and data types
for i, df in enumerate(combined_df_list):
    print(f"Columns in DataFrame {i+1}: {df.columns}")

# Concatenate the list of DataFrames into a single DataFrame
combined_df = pd.concat(combined_df_list, ignore_index=True)

# Print DataFrame information and head for verification
print(combined_df.info(), " | ", combined_df.head())

combined_df.to_csv('./data/weather_data_eng.csv', index=False)