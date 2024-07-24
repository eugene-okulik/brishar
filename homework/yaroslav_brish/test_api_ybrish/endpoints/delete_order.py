import requests
import allure
from endpoints.endpoint_handler import EndpointHandler


class DeleteOrder(EndpointHandler):

    @allure.step('Delete just created order')
    def delete_order(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{post_id}'
        )
        self.response_json = self.response.json()
        return self.response

    @allure.step('Verify that order is deleted')
    def check_deleted_order_is_deleted(self, post_id):
        get_response = requests.get(f'{self.url}/{post_id}')
        assert get_response.status_code == 404, (
            f"Expected 404, got {get_response.status_code}"
        )
