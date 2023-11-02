import requests
import allure

from data import url


class TestGetOrdersList:

    @allure.title('Test of receiving the orders list')
    @allure.description('Test of the endpoint "Получение списка заказов" GET /api/v1/orders.'
                        'Checks that a list of orders is returned in the response body')
    def test_get_orders_list(self):
        response = requests.get(f'{url}/api/v1/orders')
        assert response.status_code == 200, f'Failed to get orders list , code {response.status_code}'
        assert isinstance(response.json()["orders"], list), f'Wrong orders list type, {type(response.json()["orders"])}'
