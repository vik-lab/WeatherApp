import unittest
from unittest.mock import patch
from datetime import datetime
from weather_app import WeatherApp

class TestWeatherApp(unittest.TestCase):
    @patch('weather_app.requests.get')
    def test_get_weather_data_success(self, mock_get):
        #mock api response
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {
                'temp': 20,
                'temp_min': 15,
                'temp_max': 25
            },
            'weather': [{'description': 'Cloudy'}],
            'timezone': 3600,
            'visibility': 10000
        }

        #initialise the weather app
        weather_app = WeatherApp()

        #Test get_weather_data method
        city = 'New York'
        weather_data = weather_app.get_weather_data(city)

        #assertions
        self.assertIsNotNone(weather_data)
        self.assertEqual(weather_data['main']['temp'], 20)
        self.assertEqual(weather_data['main']['temp_min'], 15)
        self.assertEqual(weather_data['main']['temp_max'], 25)
        self.assertEqual(weather_data['weather'][0]['description'], 'Cloudy')
        self.assertEqual(weather_data['timezone'], 3600)
        self.assertEqual(weather_data['visibility'], 10000)

    @patch('weather_app.requests.get')
    def test_get_weather_data_failure(self, mock_get):
        # Mock API response
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        # Initialize WeatherApp
        weather_app = WeatherApp()

        # Test get_weather_data method with invalid city
        city = 'Invalid City'
        weather_data = weather_app.get_weather_data(city)

        # Assertions
        self.assertIsNone(weather_data)

if __name__ == '__main__':
    unittest.main()