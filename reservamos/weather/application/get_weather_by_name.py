import asyncio
import time

from weather.domain.places_api import PlacesAPI
from weather.domain.weather_api import WeatherAPI


class GetWeatherByName:

    def __init__(self, places_api: PlacesAPI, weather_api: WeatherAPI):
        self.places_api = places_api
        self.weather_api = weather_api

    async def execute(self, name: str):
        start_time = time.time()
        response = []

        places = self.places_api.get_place_by_name(name=name)

        if len(places) > 0:
            tasks_get_weathers = []
            lat = places[0]['lat']
            lon = places[0]['long']

            tasks_get_weathers.append(self.weather_api.get_weathers_by_lat_and_lon(lat=lat, lon=lon))

            weathers = await asyncio.gather(*tasks_get_weathers)

            for place, weathers_current_place in zip(places, weathers):
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

            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Tiempo de ejecución: {elapsed_time} segundos")
        return response