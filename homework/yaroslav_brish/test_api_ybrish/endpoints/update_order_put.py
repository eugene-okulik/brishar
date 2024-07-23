import requests
import allure
from endpoints.endpoint_handler import EndpointHandler


class UpdateOrderPut(EndpointHandler):

    @allure.step('Fully update new order')
    def put_order(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
