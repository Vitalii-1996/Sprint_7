import pytest
from helpers import generate_random_courier_payload
from methods.courier_methods import CourierMethods
import data
import allure


class TestCreateCourier:
    @allure.title("Test successful new courier creation")
    def test_create_courier(self):
        courier_api = CourierMethods()
        courier_payload = generate_random_courier_payload()
        status_code, response = courier_api.post_courier(courier_payload)
        assert status_code == 201
        assert response['ok']

    @allure.title("Test prohibited to create two same couriers")
    def test_create_two_same_courier(self):
        courier_api = CourierMethods()
        courier_payload = generate_random_courier_payload()
        courier_api.post_courier(courier_payload)
        status_code, response = courier_api.post_courier(courier_payload)
        assert status_code == 409
        assert response['message'] == data.CREATE_COURIER_TWICE_ERROR_MESSAGE

    @allure.title("Test successfull new courier creation only with required fields")
    def test_create_courier_with_only_required_fields(self):
        courier_api = CourierMethods()
        courier_payload = generate_random_courier_payload()
        del courier_payload['firstName']
        status_code, response = courier_api.post_courier(courier_payload)
        assert status_code == 201
        assert response['ok']

    @allure.title("Test prohibited to create new courier without required field")
    @pytest.mark.parametrize(
            'requierd_field',
            ['login', 'password']
    )
    def test_create_courier_fail_if_required_field_missing(self, requierd_field):
        courier_api = CourierMethods()
        courier_payload = generate_random_courier_payload()
        del courier_payload[requierd_field]
        status_code, response = courier_api.post_courier(courier_payload)
        assert status_code == 400
        assert response['message'] == data.CREATE_COURIER_MISSING_FIELD_ERROR

    @allure.title("Test prohibited to create new courier with exisitng login")    
    def test_create_courier_with_existing_login(self, new_courier):
        courier_api = CourierMethods()
        courier_data = new_courier
        new_courier_data = generate_random_courier_payload()
        new_courier_data['login'] = courier_data['login']
        status_code, response = courier_api.post_courier(new_courier_data)
        assert status_code == 409
        assert response['message'] == data.CREATE_COURIER_TWICE_ERROR_MESSAGE           
        