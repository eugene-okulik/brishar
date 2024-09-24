import pytest
from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker()


def select_date(page: Page, year: str, month: str, day: str):
    """Функция для выбора даты в calendar picker"""
    page.click('#dateOfBirthInput')
    page.select_option('.react-datepicker__year-select', year)
    page.select_option('.react-datepicker__month-select', month)
    page.click(
        f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']"
    )


def select_subject(page: Page, subject_name: str):
    """Функция для ввода текста в поле 'Subjects'
    и выбора подходящего варианта из выпадающего списка"""
    subjects_input = page.locator('#subjectsInput')
    subjects_input.fill(subject_name)
    suggestion = page.locator(
        f"//div[contains(@class, 'subjects-auto-complete__option')"
        f" and text()='{subject_name}']"
    )
    suggestion.click()


@pytest.mark.parametrize("year, month, day", [
    ('1990', 'July', '15'),
])
def test_form_fill_in(page: Page, year: str, month: str, day: str):
    page.goto('https://demoqa.com/automation-practice-form')

    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_email = fake.email()
    fake_phone_number = fake.msisdn()[:10]
    fake_address = fake.address()

    page.get_by_placeholder('First Name').fill(fake_first_name)
    page.get_by_placeholder('Last Name').fill(fake_last_name)
    page.get_by_placeholder('name@example.com').fill(fake_email)
    page.locator('label[for="gender-radio-1"]').click()
    page.get_by_placeholder('Mobile Number').fill(fake_phone_number)
    select_date(page, year, month, day)
    select_subject(page, 'Maths')
    page.locator('//label[contains(text(), "Sports")]').click()
    page.get_by_placeholder('Current Address').fill(fake_address)

    # Выбор штата и города
    page.locator('#state').click()
    page.locator('//div[text()="NCR"]').click()
    page.locator('#city').click()
    page.locator('//div[text()="Delhi"]').click()

    page.locator('#submit').click()

    # Ожидание модального окна с результатом
    modal = page.locator('.modal-content')
    expect(modal).to_be_visible()
