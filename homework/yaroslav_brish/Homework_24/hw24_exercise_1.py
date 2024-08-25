from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_new_tab(driver):
    driver.get('https://www.demoblaze.com/index.html')
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    # Шаг 1: Открываем товар в новой вкладке
    product_card = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Samsung galaxy s6'))
    )
    actions.key_down(Keys.CONTROL)
    actions.click(product_card)
    actions.key_up(Keys.CONTROL)
    actions.perform()

    # Переключаемся на новую вкладку
    driver.switch_to.window(driver.window_handles[1])

    # Шаг 3: Добавьте товар в корзину
    add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@onclick='addToCart(1)']"))
    )
    add_to_cart_button.click()

    # Подтверждаем добавление товара в корзину
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    # Шаг 4: Закрываем вкладку с товаром
    driver.close()

    # Переключаемся обратно на начальную вкладку
    driver.switch_to.window(driver.window_handles[0])

    # Шаг 5: Открываем корзину
    cart_button = driver.find_element(By.ID, "cartur")
    cart_button.click()

    # Шаг 6: Убеждаемся, что в корзине тот товар, который мы добавляли
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[text()='Samsung galaxy s6']")
        )
    )
    product_in_cart = driver.find_element(
        By.XPATH, "//td[text()='Samsung galaxy s6']"
    )

    assert product_in_cart is not None, "Товар не был добавлен в корзину"
