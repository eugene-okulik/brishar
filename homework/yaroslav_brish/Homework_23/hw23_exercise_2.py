from selenium import webdriver
import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


fake = Faker()


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def scroll_to_element(driver, element):
    """Скроллит страницу к указанному элементу,
    чтобы он оказался в поле зрения"""
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                          element)


def select_subject(driver, subject_name):
    """Функция для ввода текста в поле 'Subjects'
    и выбора подходящего варианта из выпадающего списка"""
    subjects_input = driver.find_element(By.ID, 'subjectsInput')
    subjects_input.send_keys(subject_name)

    # Дождаться появления выпадающего списка и выбрать первый вариант
    wait = WebDriverWait(driver, 10)
    first_suggestion = wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            f"//div[contains(@class, 'subjects-auto-complete__option')"
            f" and text()='{subject_name}']"
        ))
    )
    first_suggestion.click()


def select_date(driver, year, month, day):
    """Функция для выбора даты в calendar picker"""

    # Клик по полю даты, чтобы открыть календарь
    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()

    # Выбор года
    year_dropdown = driver.find_element(By.CLASS_NAME,
                                        'react-datepicker__year-select')
    select_year = Select(year_dropdown)
    select_year.select_by_visible_text(year)

    # Выбор месяца
    month_dropdown = driver.find_element(By.CLASS_NAME,
                                         'react-datepicker__month-select')
    select_month = Select(month_dropdown)
    select_month.select_by_visible_text(month)

    # Выбор дня
    day_element = driver.find_element(
        By.XPATH,
        f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']"
    )
    day_element.click()


def test_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    wait = WebDriverWait(driver, 10)

    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_email = fake.email()
    fake_phone_number = fake.msisdn()[:10]
    fake_address = fake.address()

    first_name = driver.find_element(By.ID, 'firstName')
    last_name = driver.find_element(By.ID, 'lastName')
    email = driver.find_element(By.XPATH, '//*[@id="userEmail"]')
    gender = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
    mobile = driver.find_element(By.XPATH, '//*[@id="userNumber"]')
    hobbies = driver.find_element(
        By.XPATH, '//label[contains(text(), "Sports")]'
    )
    address = driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
    state = driver.find_element(By.ID, 'state')
    city = driver.find_element(By.ID, 'city')
    submit_button = driver.find_element(By.ID, 'submit')

    first_name.send_keys(fake_first_name)
    last_name.send_keys(fake_last_name)
    email.send_keys(fake_email)
    gender.click()
    mobile.send_keys(fake_phone_number)

    scroll_to_element(driver, hobbies)

    select_date(driver, '1990', 'July', '15')

    select_subject(driver, 'Maths')

    hobbies.click()
    address.send_keys(fake_address)

    state.click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']"))
    ).click()

    city.click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Delhi']"))
    ).click()

    # Отправка формы
    submit_button.click()

    result_modal = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
    )
    print("Modal Content:\n", result_modal.text)
