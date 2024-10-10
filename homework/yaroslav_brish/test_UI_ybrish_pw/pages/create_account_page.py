from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from playwright.sync_api import expect


class CreateAccount(BasePage):
    page_url = '/customer/account/create'

    def enter_first_name(self, first_name):
        first_name_field = self.find(loc.first_name_loc)
        first_name_field.fill(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.find(loc.last_name_loc)
        last_name_field.fill(last_name)

    def enter_email(self, email):
        email_field = self.find(loc.email_loc)
        email_field.fill(email)

    def enter_password(self, password):
        password_field = self.find(loc.password_loc)
        password_field.press_sequentially(password, delay=150)

    def confirm_password(self, password):
        confirm_password_field = self.find(loc.confirm_password_loc)
        confirm_password_field.press_sequentially(password, delay=150)

    def click_create_button(self):
        self.find(loc.create_button_loc).click()

    def check_alert_appears(self, alert_text):
        self.page.wait_for_selector(loc.alert_loc, timeout=5000)
        locator = self.find(loc.alert_loc)
        expect(locator).to_contain_text(alert_text)

    def check_password_is_weak(self, password):
        self.enter_password(password)
        self.confirm_password(password)
        self.page.wait_for_selector(loc.password_strength_loc, timeout=5000)
        locator = self.find(loc.password_strength_loc)
        expect(locator).to_have_text("Weak")
