import pytest

from weather.application.get_weather_by_name import GetWeatherByName
from weather.domain.places_api import PlacesAPI
from weather.domain.weather_api import WeatherAPI


class PlacesAPITestSuccess(PlacesAPI):

    def get_place_by_name(self, name):
        return [
            {'id': 19, 'slug': 'monterrey', 'city_slug': 'monterrey', 'display': 'Monterrey',
             'ascii_display': 'monterrey', 'city_name': 'Monterrey', 'city_ascii_name': 'monterrey',
             'state': 'Nuevo León', 'country': 'México', 'lat': '25.6866142', 'long': '-100.3161126',
             'result_type': 'city', 'popularity': '0.365111433802639', 'sort_criteria': 0.7460445735210556}
        ]

class PlacesAPITestError(PlacesAPI):

    def get_place_by_name(self, name):
        return None


class WeatherAPITestSuccess(WeatherAPI):

    async def get_weathers_by_lat_and_lon(self, lat: float, lon: float):
        return {
            "lat": 33.44,
            "lon": -94.04,
            "timezone": "America/Chicago",
            "timezone_offset": -21600,
            "current": {
                "dt": 1618317040,
                "sunrise": 1618282134,
                "sunset": 1618333901,
                "temp": 284.07,
                "feels_like": 282.84,
                "pressure": 1019,
                "humidity": 62,
                "dew_point": 277.08,
                "uvi": 0.89,
                "clouds": 0,
                "visibility": 10000,
                "wind_speed": 6,
                "wind_deg": 300,
                "weather": [
                    {
                        "id": 500,
                        "main": "Rain",
                        "description": "light rain",
                        "icon": "10d"
                    }
                ],
                "rain": {
                    "1h": 0.21
                }
            },
            "daily": [
                {
                    "dt": 1618308000,
                    "sunrise": 1618282134,
                    "sunset": 1618333901,
                    "moonrise": 1618284960,
                    "moonset": 1618339740,
                    "moon_phase": 0.04,
                    "temp": {
                        "day": 279.79,
                        "min": 275.09,
                        "max": 284.07,
                        "night": 275.09,
                        "eve": 279.21,
                        "morn": 278.49
                    },
                    "feels_like": {
                        "day": 277.59,
                        "night": 276.27,
                        "eve": 276.49,
                        "morn": 276.27
                    },
                    "pressure": 1020,
                    "humidity": 81,
                    "dew_point": 276.77,
                    "wind_speed": 3.06,
                    "wind_deg": 294,
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "clouds": 56,
                    "pop": 0.2,
                    "rain": 0.62,
                    "uvi": 1.93
                },
            ]
        }

class WeatherAPITestError(WeatherAPI):

    async def get_weathers_by_lat_and_lon(self, lat: float, lon: float):
        return None


@pytest.mark.asyncio
async def test_happy_path():
    name = 'monterrey'
    use_case = GetWeatherByName(places_api=PlacesAPITestSuccess(), weather_api=WeatherAPITestSuccess())

    result = await use_case.execute(name=name)
    assert result == [{'city_name': 'Monterrey', 'display': 'Monterrey', 'sort_criteria': 0.7460445735210556, 'weather': [{'dt': 1618308000, 'temp_min': 275.09, 'temp_max': 284.07}]}]

@pytest.mark.asyncio
async def test_not_return_data_places_api():
    name = 'monterrey'
    use_case = GetWeatherByName(places_api=PlacesAPITestError(), weather_api=WeatherAPITestSuccess())

    result = await use_case.execute(name=name)
    assert result == []


@pytest.mark.asyncio
async def test_not_return_data_weather_api():
    name = 'monterrey'
    use_case = GetWeatherByName(places_api=PlacesAPITestSuccess(), weather_api=WeatherAPITestError())

    result = await use_case.execute(name=name)
    assert result == [{'city_name': 'Monterrey', 'display': 'Monterrey', 'sort_criteria': 0.7460445735210556, 'weather': []}]
