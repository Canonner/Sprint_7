import requests
import random
import string
import pytest

from data import url


# Фикстура для генерации данных нового курьера и создания курьера
@pytest.fixture()
def new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{url}/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    print(f'Создан курьер с данными {login_pass}')

    yield response, login_pass


# Фикстура для авторизации курьера и получения ID
@pytest.fixture()
def authorize_courier(new_courier):
    response, login_pass = new_courier

    payload_login = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    login_courier = requests.post(f'{url}/api/v1/courier/login', data=payload_login)
    courier_id = login_courier.json().get("id")

    print(f'Курьер с логином {login_pass[0]} получил id={courier_id} и авторизован')

    yield courier_id


# Фикстура для удаления курьера
@pytest.fixture()
def delete_courier(authorize_courier):
    courier_id = authorize_courier
    requests.delete(f'{url}/api/v1/courier/{courier_id}')

    print(f'Курьер с id={courier_id} был успешно удален.')
