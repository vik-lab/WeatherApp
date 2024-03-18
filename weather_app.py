from datetime import datetime, timezone
from geopy.geocoders import Nominatim
import pytz
import requests

class WeatherApp:
    def get_weather_data(self, city):
        #api key from the weather app 
        api_key = "9069e2b07eac876718deb04750b72084"
        #Get user input for city name - Prompt the user to enter the city name for which they want to get the weather:
        #city = input("Enter city name: ")
        #Define the API endpoint for the current weather data
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        #Make API request 
        response = requests.get(api_url)
        #Handle API response - Check if the API request was successful (status code 200):
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
            #process weather data here
        else:
            print("Error fetching weather data. Please try again.")
            return None

# Instantiate WeatherApp
weather_app = WeatherApp()

# Get user input for city name
city = input("Enter city name: ")

# Get weather data for the city
weather_data = weather_app.get_weather_data(city)

# Display weather information
if weather_data:
    city_time = datetime.now()
    print(f"Weather in {city}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Min Temperature: {weather_data['main']['temp_min']}°C")
    print(f"Max Temperature: {weather_data['main']['temp_max']}°C")
    print(f"Description: {weather_data['weather'][0]['description']}")
    print(f"Timezone: {weather_data['timezone']}")
    print(f"Time Now: {city_time}")
    print(f"Visibility: {weather_data['visibility']}")
    #timezone_offset = weather_data['timezone']  # Timezone offset in seconds
    #current_utc_time = datetime.now(datetime.timezone.utc)  # Get current UTC time
    #current_local_time = current_utc_time + datetime.timedelta(seconds=timezone_offset)  # Convert to local time
    #print(f"Local time in {city}: {current_local_time.strftime('%Y-%m-%d %H:%M:%S')}")
    #print("JSON Response:")
    #print(weather_data)