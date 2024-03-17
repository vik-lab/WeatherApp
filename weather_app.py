from datetime import datetime, timezone
from geopy.geocoders import Nominatim
import pytz
import requests

#api key from the weather app 
api_key = "9069e2b07eac876718deb04750b72084"

"""def get_country_by_city(city_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city_name)
    if location:
        return location.address.split(',')[-1].strip()
    else:
        return None"""

#Get user input for city name - Prompt the user to enter the city name for which they want to get the weather:
city = input("Enter city name: ")
#country = input("Enter the country name: ")
#country = get_country_by_city(city)
#Define the API endpoint for the current weather data
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

#Make API request - Replace {{CITY_NAME}} in the API URL with the user's input:
#url = api_url.replace('{{CITY_NAME}}', city)
response = requests.get(api_url)

#Handle API response - Check if the API request was successful (status code 200):
if response.status_code == 200:
    weather_data = response.json()
    #process weather data here
else:
    print("Error fetching weather data. Please try again.")

#Display weather information- Extract relevant information from the API response and display it to the user: 
if response.status_code == 200:
    weather_data = response.json()
    cityTime = datetime.now()

    #cityTempDateTime = datetime.now(pytz.timezone('{country}/{city}'))
    #timezone = weather_data['timezone']

    print(f"Weather in {city}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"MinTemperature: {weather_data['main']['temp_min']}°C")
    print(f"MaxTemperature: {weather_data['main']['temp_max']}°C")
    print(f"Description: {weather_data['weather'][0]['description']}")
    print(f"Timezone: {weather_data ['timezone']}")
    print(f"TimeNow:", cityTime)
    #print(f"TimeInRequestedCity:", cityTempDateTime)
    print(f"Visibility: {weather_data ['visibility']}")
    
   ## timezone_offset = weather_data['timezone']  # Timezone offset in seconds
   # current_utc_time = datetime.now(datetime.timezone.utc)  # Get current UTC time
    #current_local_time = current_utc_time + datetime.timedelta(seconds=timezone_offset)  # Convert to local time
    #print(f"Local time in {city}: {current_local_time.strftime('%Y-%m-%d %H:%M:%S')}")
    #print("JSON Response:")
    #print(weather_data)