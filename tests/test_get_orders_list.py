import requests
from data import url


class TestGetOrdersList:

    def test_get_orders_list(self):

        response = requests.get(f'{url}/api/v1/orders')

        assert response.status_code == 200 and isinstance(response.json()["orders"], list), \
            (f'Failed to get orders list , code {response.status_code} '
             f'or orders list is not a list, type({response.json()["orders"]}')
