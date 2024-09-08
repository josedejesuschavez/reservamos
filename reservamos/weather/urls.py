from django.urls import path
from .views import WeathersAPIView, WeatherAPIView

urlpatterns = [
    path('weathers/', WeathersAPIView.as_view(), name='weathers_api'),
    path('weather/', WeatherAPIView.as_view(), name='weather_api'),
]