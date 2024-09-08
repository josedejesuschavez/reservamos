import requests

from weather.domain.places_api import PlacesAPI


class ReservamosPlacesApi(PlacesAPI):
    def __init__(self):
        self.url = 'https://search.reservamos.mx/api/v2/places'

    def get_place_by_name(self, name):
        params = {
            'q': name  # Esta es la ciudad o palabra clave que estás buscando
        }

        response = requests.get(self.url, params=params)

        if response.status_code == 201:
            data = response.json()
        else:
            data = None

        return data