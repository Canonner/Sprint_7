import requests
import pytest
import allure

from data import url


class TestCourierLogin:

    @allure.title('Test of successful login of unique courier')
    @allure.description('Positive test of the endpoint "Логин курьера в системе" POST /api/v1/courier/login.'
                        'Checks successful authorization of a courier')
    def test_successful_courier_login(self, new_courier):
        response, login_pass = new_courier
        payload_login = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(f'{url}/api/v1/courier/login', data=payload_login)
        assert response.status_code == 200, f'Failed to login courier, code {response.status_code}'
        assert "id" in response.text, f'No "id" field in response body'

    @allure.title('Test of failed attempt to login with the missing field')
    @allure.description('Negative test of the endpoint "Логин курьера в системе" POST /api/v1/courier/login.'
                        'Parameterized test, checks impossibility of authorization '
                        'when any of the mandatory fields is missing')
    @pytest.mark.parametrize("login_missing", [True, False])
    def test_login_with_any_missing_field_failed(self, new_courier, login_missing):
        login_pass = new_courier[1]
        payload = {}
        if not login_missing:
            payload["login"] = login_pass[0]
        else:
            payload["password"] = login_pass[1]
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        assert response.status_code == 400, f'Instead of an error code 400 received code {response.status_code}'
        assert response.text == '"message":  "Недостаточно данных для входа"', f'Error message contains wrong text'

    @allure.title('Test of failed attempt to login with the wrong fields')
    @allure.description('Negative test of the endpoint "Логин курьера в системе" POST /api/v1/courier/login.'
                        'Parameterized test, checks impossibility of authorization '
                        'when any of the mandatory fields is wrong')
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
        assert response.status_code == 404, f'Instead of an error code 404 received code {response.status_code}'
        assert response.text == '"message": "Учетная запись не найдена"', f'Error message contains wrong text'
