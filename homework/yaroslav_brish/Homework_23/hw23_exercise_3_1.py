from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_dropdown(driver):
    language_to_select = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    wait = WebDriverWait(driver, 10)
    select = wait.until(EC.element_to_be_clickable(
        (By.ID, 'id_choose_language'))
    )
    dropdown = Select(select)
    dropdown.select_by_visible_text('Python')

    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()

    result_text = wait.until(
        EC.visibility_of_element_located((By.ID, 'result-text'))
    )

    assert result_text.text == language_to_select,  \
        f"Expected text {language_to_select}, but fond '{result_text.text}'"
