import requests
from json import JSONDecodeError
from data import BASE_URL, COURIER_URL

class CourierMethods:
    def post_courier(self, params):
        response = requests.post(
            f'{BASE_URL}{COURIER_URL}', json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
        
    def post_login(self, params):
        response = requests.post(
            f'{BASE_URL}{COURIER_URL}/login', json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
        
    def delete_courier(self, id):
        response = requests.delete(
            f'{BASE_URL}{COURIER_URL}/{id}'
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text