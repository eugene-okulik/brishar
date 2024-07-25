import random
from locust import task, HttpUser


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


class Orders(HttpUser):
    BASE_URL = 'https://api.restful-api.dev/objects'
    obj_id = None

    @task(3)
    def create_order(self):
        body = random.choice(test_data)
        headers = {"content-type": "application/json"}
        response = self.client.post(self.BASE_URL,
                                    json=body,
                                    headers=headers)
        self.obj_id = response.json()['id']

    @task(2)
    def update_order_put(self):
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
        self.client.put(f'{self.BASE_URL}/{self.obj_id}',
                        json=body,
                        headers=headers)

    @task(2)
    def update_order_patch(self):
        body = {
            "name": "Apple MacBook Pro 16 (Updated Name)"
        }
        headers = {"content-type": "application/json"}
        self.client.patch(f'{self.BASE_URL}/{self.obj_id}',
                          json=body,
                          headers=headers)

    @task(1)
    def delete_order(self):
        self.client.delete(f'{self.BASE_URL}/{self.obj_id}')
