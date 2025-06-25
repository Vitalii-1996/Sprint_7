from methods.order_methods import OrderMethods


class TestCreateOrder:
    def test_create_order_choose_color(self, accept_new_order):
        order_api = OrderMethods()
        params = {
            "courierId": accept_new_order
        }
        status_code, response = order_api.get_orders(params)
        assert status_code == 200
        assert len(response['orders']) > 0