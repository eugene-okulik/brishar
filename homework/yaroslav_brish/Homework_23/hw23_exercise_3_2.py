from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_text_after_loading(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    wait = WebDriverWait(driver, 10)
    start_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Start"]'))
    )
    start_button.click()

    hello_world_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//h4[text()="Hello World!"]')
        )
    )

    assert hello_world_text.text == "Hello World!", \
        f"Expected text 'Hello World!', but fond '{hello_world_text.text}'"
