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


test_data = [
    {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "Dell XPS 15",
        "data": {
            "year": 2020,
            "price": 1499.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB"
        }
    },
    {
        "name": "HP Spectre x360",
        "data": {
            "year": 2021,
            "price": 1249.99,
            "CPU model": "Intel Core i5",
            "Hard disk size": "256 GB"
        }
    }
]


# POST запрос
@pytest.mark.critical
@pytest.mark.parametrize("body", test_data)
def test_add_object(body, start_testing, testcase_borders):
    headers = {"content-type": "application/json"}
    response = requests.post(BASE_URL, json=body, headers=headers)
    response_data = response.json()
    assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    assert response_data["name"] == body["name"], "Names do not match"


# PUT запрос
def test_update_object(new_obj_id, testcase_borders):
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.put(f'{BASE_URL}/{new_obj_id}',
                            json=body,
                            headers=headers)
    response_data = response.json()
    assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    assert response_data["data"]["color"] == "silver", "Color was not updated"


# PATCH запрос
@pytest.mark.medium
def test_partially_update_object(new_obj_id, testcase_borders):
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {"content-type": "application/json"}
    response = requests.patch(f'{BASE_URL}/{new_obj_id}',
                              json=body,
                              headers=headers)
    response_data = response.json()
    assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    assert response_data["name"] == body["name"], "Name was not updated"


# DELETE запрос
def test_delete_object(new_obj_id, testcase_borders):
    response = requests.delete(f'{BASE_URL}/{new_obj_id}')
    assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    # Проверяем, что объект действительно удален
    get_response = requests.get(f'{BASE_URL}/{new_obj_id}')
    assert get_response.status_code == 404, (f"Expected 404, "
                                             f"got {get_response.status_code}")
