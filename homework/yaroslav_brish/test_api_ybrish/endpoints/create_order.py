import requests
import allure
from endpoints.endpoint_handler import EndpointHandler


class CreateOrder(EndpointHandler):

    @allure.step('Create new order')
    def create_new_order(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
