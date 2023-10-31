import requests
import json
import pytest

from data import url, OrderData


class TestOrderCreation:

    @pytest.mark.parametrize('color', OrderData.colors)
    def test_order_creation_variate_colors(self, color):

        order_data = OrderData(color)
        payload_order = order_data.payload_order

        response = requests.post(f'{url}/api/v1/orders', data=json.dumps(payload_order))
        assert response.status_code == 201 and "track" in response.text, \
            f'Failed to create order with color {color}'
