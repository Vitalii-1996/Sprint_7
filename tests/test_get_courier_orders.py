from methods.order_methods import OrderMethods
import allure


class TestGetCourierOrder:
    @allure.title('Test get courier order and check orders length')
    def test_get_courier_orders(self, accept_new_order):
        order_api = OrderMethods()
        params = {
            "courierId": accept_new_order
        }
        status_code, response = order_api.get_orders(params)
        assert status_code == 200
        assert len(response['orders']) > 0
        