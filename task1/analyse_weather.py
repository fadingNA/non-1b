import combine_weather
from combine_weather import *

WIND_SPEED_THRESHOLD = 50.0
# > 50 km/h is considered Wind storm
SNOW_PRECIP_THRESHOLD = 30.0
# > 30 mm is considered Snow storm
RAIN_PRECIP_THRESHOLD = 20.0
# > 20 mm is considered Rain storm


severe_wind_days = combined_df[combined_df['WIND_SPEED']
                               > WIND_SPEED_THRESHOLD]

winter_storm_days = combined_df[(combined_df['type'] == 'snow') & (
    combined_df['PRECIP_AMOUNT'] >= SNOW_PRECIP_THRESHOLD)]

rainny_storm = combined_df[(combined_df['type'] == 'rain') & (combined_df['PRECIP_AMOUNT'] >= RAIN_PRECIP_THRESHOLD)]


print(f"Number of severe wind days: {severe_wind_days.shape[0]}")
