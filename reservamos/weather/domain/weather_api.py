from abc import ABC, abstractmethod


class WeatherAPI(ABC):

    @abstractmethod
    def get_weathers_by_lat_and_lon(self, lat: float, lon: float):
        pass
