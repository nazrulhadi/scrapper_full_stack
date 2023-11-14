from geopy.geocoders import Nominatim
import csv
import pandas as pd

def address_to_coordinates(address):
    geolocator = Nominatim(user_agent="MyGeocodingApp/1.0")  # Replace "your_app_name" with a unique user agent
    location = geolocator.geocode(address)

    if location:
        latitude, longitude = location.latitude, location.longitude
        return latitude, longitude
    else:
        location = geolocator.geocode("Taman Melaka Raya")
        latitude, longitude = location.latitude, location.longitude
        return latitude, longitude


# Specify the file path
csv_file_path = '/workspace/zus_scrapper/outlet.csv'
location = []
df = pd.read_csv(csv_file_path)

# Use regex to extract values after '-' or take the whole word
extracted_values = df['outlet_name'].str.extract(r'–\s*(.*)').squeeze()

# Fill NaN values with the original values
df['Extracted_Value'] = extracted_values.combine_first(df['outlet_name'])

# Display the updated DataFrame
df[['Latitude', 'Longitude']]   = df['Extracted_Value'].apply(lambda x: pd.Series(address_to_coordinates(x)))

df.to_csv('outlets_with_coordinates.csv', index=False)