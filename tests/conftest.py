import requests
import random
import string
import pytest

from data import url


@pytest.fixture()
def new_courier():
    letters = string.ascii_lowercase

    login_pass = []

    login = ''.join(random.choice(letters) for _ in range(10))
    password = ''.join(random.choice(letters) for _ in range(10))
    first_name = ''.join(random.choice(letters) for _ in range(10))

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

    yield response, login_pass

    payload_login = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    login_courier = requests.post(f'{url}/api/v1/courier/login', data=payload_login)
    courier_id = login_courier.json().get("id")
    requests.delete(f'{url}/api/v1/courier/{courier_id}')
