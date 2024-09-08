from rest_framework import status
from rest_framework.response import Response
from adrf.views import APIView

from weather.application.get_weather_by_name import GetWeatherByName
from weather.application.get_weathers_by_name import GetWeathersByName
from weather.infrastructure.open_weather_2_5_weather_api import OpenWeatherWeatherAPI
from weather.infrastructure.reservamos_places_api import ReservamosPlacesApi


class WeathersAPIView(APIView):

    async def get(self, request, format=None):
        name = request.query_params.get('name', None)

        if not name:
            return Response({'error': 'Se requiere un parámetro de ciudad.'}, status=status.HTTP_400_BAD_REQUEST)

        use_case = GetWeathersByName(places_api=ReservamosPlacesApi(), weather_api=OpenWeatherWeatherAPI())
        result = await use_case.execute(name=name)
        return Response(result, status=status.HTTP_200_OK)

class WeatherAPIView(APIView):

    async def get(self, request, format=None):
        name = request.query_params.get('name', None)

        if not name:
            return Response({'error': 'Se requiere un parámetro de ciudad.'}, status=status.HTTP_400_BAD_REQUEST)

        use_case = GetWeatherByName(places_api=ReservamosPlacesApi(), weather_api=OpenWeatherWeatherAPI())
        result = await use_case.execute(name=name)
        return Response(result, status=status.HTTP_200_OK)
