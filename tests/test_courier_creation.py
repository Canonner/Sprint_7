import requests
import pytest
from data import url, CourierData


class TestCourierCreation:

    def test_successful_courier_creation(self, new_courier):
        response = new_courier[0]
        assert (response.status_code == 201
                and response.json() == {"ok": True}), f"Failed to create new courier, code {response.status_code}"

    def test_creation_repeating_courier_failed(self, new_courier):
        repeating_courier_payload = {
            "login": new_courier[1][0],
            "password": new_courier[1][1],
            "firstName": new_courier[1][2]
        }
        response = requests.post(f'{url}/api/v1/courier', data=repeating_courier_payload)
        assert (response.status_code == 409
                and response.json() == {"message": "Этот логин уже используется"}), \
            f'Instead of an error code 409 received code {response.status_code} or error message contains wrong text'

    @pytest.mark.parametrize('payload', CourierData.creation_missing_fields)
    def test_creation_with_any_missing_field_failed(self, payload):
        response = requests.post(f'{url}/api/v1/courier', data=payload)
        assert (response.status_code == 400
                and response.text == '"message": "Недостаточно данных для создания учетной записи"'), \
            f'Wrong code or wrong error message'

    def test_creation_courier_with_repeating_login_failed(self, new_courier):
        repeating_login_payload = {
            "login": new_courier[1][0],
            "password": new_courier[1][1]+'a',
            "firstName": new_courier[1][2]
        }
        print(repeating_login_payload)
        response = requests.post(f'{url}/api/v1/courier', data=repeating_login_payload)
        assert (response.status_code == 409
                and response.json() == {"message": "Этот логин уже используется"}), \
            f'Unable to return an error code 409, code {response.status_code} instead'
