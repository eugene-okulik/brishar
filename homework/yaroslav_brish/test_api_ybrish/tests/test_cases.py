import pytest


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
@pytest.mark.parametrize("body", test_data)
def test_add_object(create_order_endpoint, body,
                    start_testing, testcase_borders):
    create_order_endpoint.create_new_order(payload=body)
    create_order_endpoint.check_status_code_is_200()
    create_order_endpoint.check_response_title_is_correct(body["name"])


# PUT запрос
def test_update_object(put_order_endpoint, new_obj_id, testcase_borders):
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
    put_order_endpoint.put_order(new_obj_id, body)
    put_order_endpoint.check_status_code_is_200()
    put_order_endpoint.check_response_title_is_correct(body["name"])


# PATCH запрос
def test_partially_update_object(patch_order_endpoint,
                                 new_obj_id, testcase_borders):
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    patch_order_endpoint.patch_order(new_obj_id, body)
    patch_order_endpoint.check_status_code_is_200()
    patch_order_endpoint.check_response_title_is_correct(body["name"])


# DELETE запрос

def test_delete_object(delete_order_endpoint,
                       new_obj_id, testcase_borders):
    delete_order_endpoint.delete_order(new_obj_id)
    delete_order_endpoint.check_status_code_is_200()
    delete_order_endpoint.check_deleted_order_is_deleted(
        new_obj_id
    )
