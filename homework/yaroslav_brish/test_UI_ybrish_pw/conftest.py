import pytest
from pages.create_account_page import CreateAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import SalePage
from playwright.sync_api import Page


@pytest.fixture()
def create_account_page(page: Page):
    return CreateAccount(page)


@pytest.fixture()
def eco_friendly_page(page: Page):
    return EcoFriendly(page)


@pytest.fixture()
def sale_page(page: Page):
    return SalePage(page)
