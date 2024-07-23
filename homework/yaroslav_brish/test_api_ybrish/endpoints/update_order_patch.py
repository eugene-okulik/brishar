import requests
import allure
from endpoints.endpoint_handler import EndpointHandler


class UpdateOrderPatch(EndpointHandler):

    @allure.step('Partially update new order')
    def patch_order(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
