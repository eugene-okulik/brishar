import requests
import pytest


BASE_URL = 'https://api.restful-api.dev/objects'


# Фикстура для начала и завершения всех тестов
@pytest.fixture(scope="session")
def start_testing():
    print('\nStart testing')
    yield
    print('\nTesting completed')


# Фикстура для вывода перед и после каждого теста
@pytest.fixture()
def testcase_borders():
    print('\nbefore test')
    yield
    print('\nafter test')


# Фикстура для создания нового объекта перед тестом и его удаления после теста
@pytest.fixture()
def new_obj_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1869.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.post(BASE_URL,
                             json=body,
                             headers=headers)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'{BASE_URL}/{obj_id}')
