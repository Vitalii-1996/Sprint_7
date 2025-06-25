import requests
from json import JSONDecodeError
from data import BASE_URL, ORDER_URL


class OrderMethods:
    def post_order(self, params):
        response = requests.post(
            f'{BASE_URL}{ORDER_URL}', json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    def put_accept(self, id, params):
        response = requests.put(
            f'{BASE_URL}{ORDER_URL}/accept/{id}', params=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
        
    def get_orders(self, params):
        response = requests.get(
            f'{BASE_URL}{ORDER_URL}', params=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
        
    def get_orders_track(self, params):
        response = requests.get(
            f'{BASE_URL}{ORDER_URL}/track', params=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text