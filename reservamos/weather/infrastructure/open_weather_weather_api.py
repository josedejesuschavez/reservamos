import asyncio
import requests

from reservamos.settings import API_KEY_OPEN_WEATHER
from weather.domain.weather_api import WeatherAPI


class OpenWeatherWeatherAPI(WeatherAPI):

    def __init__(self):
        self.url = 'https://api.openweathermap.org/data/2.5/onecall'
        self.api_key = API_KEY_OPEN_WEATHER

    def get_weathers_by_lat_and_lon(self, lat: float, lon: float):
        params = {
            'lat': lat,
            'lon': lon,
            'exclude': 'current,minutely,hourly,alerts',
            'units': 'metric',
            'appid': self.api_key
        }

        response = requests.get(self.url, params=params)

        if response.status_code == 200:
            data = response.json()
        else:
            data = None

        return data
