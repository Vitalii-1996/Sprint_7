from methods.order_methods import OrderMethods
import pytest
import data
import copy


class TestCreateOrder:
    @pytest.mark.parametrize(
        'colors',
        [
            ['BLACK'], 
            ['GREY'],
            ['BLACK', 'GREY'],
            []
        ]
    )
    def test_create_order_choose_color(self, colors):
        order_api = OrderMethods()
        payload = copy.deepcopy(data.ORDER_PAYLOAD)
        for color in colors:
            payload['color'].append(color)
        status_code, response = order_api.post_order(payload)
        assert status_code == 201
        assert response['track'] != None