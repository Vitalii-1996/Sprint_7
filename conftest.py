import pytest
import data
from helpers import generate_random_courier_payload
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

@pytest.fixture
def new_courier():
    courier_api = CourierMethods()
    login_pass = []
    payload = generate_random_courier_payload()
    status_code, _ = courier_api.post_courier(payload)
    
    if status_code == 201:
        del payload['firstName']
        login_pass = payload

    yield login_pass

    status_code, response = courier_api.post_login(login_pass)
    if status_code == 200:
        courier_api.delete_courier(response['id'])

@pytest.fixture()
def courier_id(new_courier):
    courier_api = CourierMethods()
    _, response = courier_api.post_login(new_courier)
    return response['id']

@pytest.fixture
def new_order_track():
    order_api = OrderMethods()
    payload = data.ORDER_PAYLOAD
    _, response = order_api.post_order(payload)
    return response['track']

@pytest.fixture
def new_order_id(new_order_track):
    order_api = OrderMethods()
    params = {
        "t": new_order_track
    }
    _, response = order_api.get_orders_track(params)
    return response['order']['id']

@pytest.fixture
def accept_new_order(courier_id, new_order_id):
    order_api = OrderMethods()
    params = {
        "courierId": courier_id
    }
    order_api.put_accept(new_order_id, params)
    return courier_id
