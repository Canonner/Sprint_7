import requests
import allure
import json
import pytest

from data import url, OrderData


class TestOrderCreation:

    @allure.title('Test of an order creation with various colors')
    @allure.description('Test of the endpoint "Создание заказа" POST /api/v1/orders.'
                        'Checks the creation of the order with various combination of colors '
                        'and that the response body contains "track".'
                        'Parameterized test, collects color data from data.py file')
    @pytest.mark.parametrize('color', OrderData.colors)
    def test_order_creation_variate_colors(self, color):
        response = requests.post(f'{url}/api/v1/orders', data=json.dumps(color))
        assert response.status_code == 201, f'Failed to create an order with {color}'
        assert "track" in response.text, f'No "track" field in response body'
