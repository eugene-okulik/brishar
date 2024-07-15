import requests
import pytest
import allure


BASE_URL = 'https://api.restful-api.dev/objects'

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
@allure.feature('Orders')
@allure.story('Create order')
@allure.title('Create a new order')
@pytest.mark.critical
@pytest.mark.parametrize("body", test_data)
def test_add_object(body, start_testing, testcase_borders):
    with allure.step('Prepare test data'):
        headers = {"content-type": "application/json"}
    with allure.step('Run request to create a post'):
        response = requests.post(BASE_URL, json=body, headers=headers)
        response_data = response.json()
    with allure.step('Verify that response code is 200'):
        assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    with allure.step('Verify that name matches "name" in request'):
        assert response_data["name"] == body["name"], "Names do not match"


# PUT запрос
@allure.feature('Orders')
@allure.story('Update order')
@allure.title('Edit the whole order')
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
@allure.feature('Orders')
@allure.story('Update order')
@allure.title('Change name in newly created order')
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
@allure.feature('Orders')
@allure.story('Delete order')
@allure.title('Delete just created order')
def test_delete_object(new_obj_id, testcase_borders):
    response = requests.delete(f'{BASE_URL}/{new_obj_id}')
    assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    # Проверяем, что объект действительно удален
    get_response = requests.get(f'{BASE_URL}/{new_obj_id}')
    assert get_response.status_code == 404, (f"Expected 404, "
                                             f"got {get_response.status_code}")
