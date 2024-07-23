import allure


class EndpointHandler:
    url = 'https://api.restful-api.dev/objects'
    response = None
    response_json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Verify that name matches "name" in request')
    def check_response_title_is_correct(self, name):
        assert self.response_json['name'] == name, "Name was not updated"

    @allure.step('Verify that response code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, "Status code is not 200"
