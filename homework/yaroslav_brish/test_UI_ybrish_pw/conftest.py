from playwright.sync_api import BrowserContext
import pytest
from pages.create_account_page import CreateAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import SalePage
from playwright.sync_api import Page


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def create_account_page(page: Page):
    return CreateAccount(page)


@pytest.fixture()
def eco_friendly_page(page: Page):
    return EcoFriendly(page)


@pytest.fixture()
def sale_page(page: Page):
    return SalePage(page)
