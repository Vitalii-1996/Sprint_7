import pytest
from helpers import generate_random_courier_payload
from methods.courier_methods import CourierMethods
import data


class TestCreateCourier:
    def test_create_courier(self, courier_id):
        courier_api = CourierMethods()
        
        status_code, response = courier_api.delete_courier(courier_id)
        assert status_code == 200
        assert response['ok']

        
