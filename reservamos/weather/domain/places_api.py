from abc import ABC, abstractmethod


class PlacesAPI(ABC):

    @abstractmethod
    def get_place_by_name(self, name):
        pass