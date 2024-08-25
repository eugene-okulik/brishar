from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_add_to_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    first_product = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item"))
    )
    add = driver.find_element(By.CLASS_NAME, 'tocompare')
    actions.move_to_element(first_product)
    actions.click(add)
    actions.perform()
    message = (By.CSS_SELECTOR, "div[data-bind*='prepareMessageForHtml']")
    wait.until(EC.text_to_be_present_in_element(message, "You added product"))
    compare_section_item = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.sidebar.sidebar-additional')
        )
    )
    product_in_compare = compare_section_item.find_element(
        By.XPATH, ".//a[contains(text(), 'Push It Messenger Bag')]"
    )

    assert product_in_compare is not None, "Товар не был добавлен к сравнению"
