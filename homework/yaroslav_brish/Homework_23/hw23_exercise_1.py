from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_text_input_and_display(driver):
    input_data = 'Text_for_TESTING'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    text_string.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    print(result_text.text)
    # print(result_text.get_attribute('innerText'))
    assert result_text.text == input_data
