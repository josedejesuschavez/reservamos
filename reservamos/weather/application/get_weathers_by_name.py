import asyncio

from weather.domain.places_api import PlacesAPI
from weather.domain.weather_api import WeatherAPI


class GetWeathersByName:

    def __init__(self, places_api: PlacesAPI, weather_api: WeatherAPI):
        self.places_api = places_api
        self.weather_api = weather_api

    def execute(self, name: str):
        response = []

        places = self.places_api.get_place_by_name(name=name)

        for place in places:
            lat = place['lat']
            lon = place['long']

            weathers_current_place = self.weather_api.get_weathers_by_lat_and_lon(lat=lat, lon=lon)

            weathers_current_place_data = []

            if weathers_current_place and weathers_current_place.get('daily'):
                for weather_current_place in weathers_current_place['daily']:
                    weather_current_place = {
                        'dt': weather_current_place['dt'],
                        'temp_min': weather_current_place['temp']['min'],
                        'temp_max': weather_current_place['temp']['max'],
                    }
                    weathers_current_place_data.append(weather_current_place)

                place_data = {
                    'city_name': place['city_name'],
                    'display': place['display'],
                    'sort_criteria': place['sort_criteria'],
                    'weather': weathers_current_place_data,
                }

                response.append(place_data)

        return response