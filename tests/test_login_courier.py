import pytest
import data
from helpers import generate_random_courier_payload
from methods.courier_methods import CourierMethods
import allure

class TestLoginCourier:
    @allure.title('Test successful courier login')
    def test_login_courier(self, new_courier):
        courier_api = CourierMethods()
        courier_data = new_courier
        status_code, response = courier_api.post_login(courier_data)
        assert status_code == 200
        assert response['id'] != None

    @allure.title('Test prohibited to login without required fields')
    @pytest.mark.parametrize(
            'requierd_field,expeted_code',
            [
                ('login',400), 
                ('password',504)
            ]
    )
    def test_login_courier_fail_if_required_field_missing(self, requierd_field, expeted_code, new_courier):
        courier_api = CourierMethods()
        courier_data = new_courier
        del courier_data[requierd_field]
        status_code, _ = courier_api.post_login(courier_data)
        assert status_code == expeted_code

    @allure.title('Test prohibited to login with wrong login or password')
    @pytest.mark.parametrize(
            'login_field',
            ['login', 'password']
    )
    def test_login_courier_wrong_login_or_password(self, login_field, new_courier):
        courier_api = CourierMethods()
        courier_data = new_courier
        random_courier = generate_random_courier_payload()
        courier_data[login_field] = random_courier[login_field]
        status_code, response = courier_api.post_login(courier_data)
        assert status_code == 404
        assert response['message'] == data.LOGIN_COURIER_NOT_FOUND_ERROR

    @allure.title('Test prohibited to login for non-existing user')
    def test_login_not_existiong_user(self):
        courier_api = CourierMethods()
        random_courier = generate_random_courier_payload()
        status_code, response = courier_api.post_login(random_courier)
        assert status_code == 404
        assert response['message'] == data.LOGIN_COURIER_NOT_FOUND_ERROR
   