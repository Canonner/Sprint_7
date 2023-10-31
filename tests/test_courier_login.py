import requests
import pytest
from data import url


class TestCourierLogin:

    def test_successful_courier_login(self, new_courier):
        response, login_pass = new_courier
        payload_login = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(f'{url}/api/v1/courier/login', data=payload_login)
        assert response.status_code == 200 and "id" in response.text

    @pytest.mark.parametrize("login_missing, password_missing", [
        (False, True),  # Тест с существующим полем "login" и отсутствующим полем "password"
        (True, False)   # Тест с отсутствующим полем "login" и существующим полем "password"
    ])
    def test_login_with_any_missing_field_failed(self, new_courier, login_missing, password_missing):
        login_pass = new_courier[1]
        payload_login = {
            "login": login_pass[0] if not login_missing else "",
            "password": login_pass[1] if not password_missing else ""
        }
        response = requests.post(f'{url}/api/v1/courier/login', data=payload_login)
        assert response.status_code == 400 and response.text == '"message":  "Недостаточно данных для входа"', \
            'Wrong code or wrong error message'

    @pytest.mark.parametrize("login_wrong, password_wrong", [
        (False, True),  # Тест с верным полем "login" и неверным полем "password"
        (True, False)   # Тест с неверным полем "login" и верным полем "password"
    ])
    def test_login_with_any_wrong_field_failed(self, new_courier, login_wrong, password_wrong):
        login_pass = new_courier[1]
        payload_login = {
            "login": login_pass[0] if not login_wrong else login_pass[0]+'a',
            "password": login_pass[1] if not password_wrong else login_pass[1]+'b'
        }
        response = requests.post(f'{url}/api/v1/courier/login', data=payload_login)
        assert response.status_code == 404 and response.text == '"message":  "Недостаточно данных для входа"', \
            'Wrong code or wrong error message'
