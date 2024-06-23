import requests

BASE_URL = 'https://api.restful-api.dev/objects'


# POST запрос
def add_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.post(BASE_URL,
                             json=body,
                             headers=headers)
    assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    response_data = response.json()
    assert response_data["name"] == body["name"], "Names do not match"
    return response_data["id"]


# PUT запрос
def update_object(obj_id):
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
    response = requests.put(f'{BASE_URL}/{obj_id}',
                            json=body,
                            headers=headers)
    assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    response_data = response.json()
    assert response_data["data"]["color"] == "silver", "Color was not updated"
    return response_data


# PATCH запрос
def partially_update_object(obj_id):
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {"content-type": "application/json"}
    response = requests.patch(f'{BASE_URL}/{obj_id}',
                              json=body,
                              headers=headers)
    assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    response_data = response.json()
    assert response_data["name"] == body["name"], "Name was not updated"
    return response_data


# DELETE запрос
def delete_object(obj_id):
    response = requests.delete(f'{BASE_URL}/{obj_id}')
    assert response.status_code == 200, (f"Expected 200, "
                                         f"got {response.status_code}")
    # Проверяем, что объект действительно удален
    get_response = requests.get(f'{BASE_URL}/{obj_id}')
    assert get_response.status_code == 404, (f"Expected 404, "
                                             f"got {get_response.status_code}")


if __name__ == "__main__":
    # Создание объекта
    created_object_id = add_object()
    print(f"Object created with ID: {created_object_id}")

    # Полное обновление объекта
    updated_object = update_object(created_object_id)
    print(f"Object updated: {updated_object}")

    # Частичное обновление объекта
    partially_updated_object = partially_update_object(created_object_id)
    print(f"Object partially updated: {partially_updated_object}")

    # Удаление объекта
    delete_object(created_object_id)
    print(f"Object with ID {created_object_id} deleted")
