import requests
import pytest
import allure

from data import url, CourierData


class TestCourierCreation:

    @allure.title('Test of successful creation of a courier')
    @allure.description('Positive test of the endpoint "Создание курьера" POST /api/v1/courier.'
                        'Checks that a courier can be created, '
                        'that all required fields must be passed to the endpoint, '
                        'and that a successful request returns {"ok":true} ')
    def test_successful_courier_creation(self, new_courier):
        response = new_courier[0]
        assert response.status_code == 201, f'Failed to create new courier, code {response.status_code}'
        assert response.json() == {"ok": True}, f'Response body contains wrong text'

    @allure.title('Test of failed attempt to create a repeating courier')
    @allure.description('Negative test of the endpoint "Создание курьера" POST /api/v1/courier.'
                        'Checks impossibility of creation of repeating courier')
    def test_creation_repeating_courier_failed(self, new_courier):
        repeating_courier_payload = {
            "login": new_courier[1][0],
            "password": new_courier[1][1],
            "firstName": new_courier[1][2]
        }
        response = requests.post(f'{url}/api/v1/courier', data=repeating_courier_payload)
        assert response.status_code == 409, f'Instead of an error code 409 received code {response.status_code}'
        assert response.json() == {"message": "Этот логин уже используется"}, f'Error message contains wrong text'

    @allure.title('Test of failed attempt to create a courier with missing fields')
    @allure.description('Negative test of the endpoint "Создание курьера" POST /api/v1/courier.'
                        'Parameterized test, checks impossibility of creation of a courier '
                        'when any of the mandatory fields is missing')
    @pytest.mark.parametrize('payload', CourierData.creation_missing_fields)
    def test_creation_with_any_missing_field_failed(self, payload):
        response = requests.post(f'{url}/api/v1/courier', data=payload)
        assert response.status_code == 400, f'Instead of an error code 400 received code {response.status_code}'
        assert response.text == '"message": "Недостаточно данных для создания учетной записи"', \
            f'Error message contains wrong text'

    @allure.title('Test of failed attempt to create a courier with repeating login')
    @allure.description('Negative test of the endpoint "Создание курьера" POST /api/v1/courier.'
                        'Checks impossibility of creation of a courier with repeating login')
    def test_creation_courier_with_repeating_login_failed(self, new_courier):
        repeating_login_payload = {
            "login": new_courier[1][0],
            "password": new_courier[1][1]+'a',
            "firstName": new_courier[1][2]
        }
        print(repeating_login_payload)
        response = requests.post(f'{url}/api/v1/courier', data=repeating_login_payload)
        assert response.status_code == 409, f'Instead of an error code 409 received code {response.status_code}'
        assert response.json() == {"message": "Этот логин уже используется"}, f'Error message contains wrong text'
