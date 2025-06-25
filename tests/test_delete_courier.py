from methods.courier_methods import CourierMethods
import allure


class TestDeleteCourier:
    @allure.title("Test successful courier deletion")
    def test_delete_courier(self, courier_id):
        courier_api = CourierMethods()
        
        status_code, response = courier_api.delete_courier(courier_id)
        assert status_code == 200
        assert response['ok']

        
