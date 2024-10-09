from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from playwright.sync_api import expect


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def click_on_product_card(self, item_number: int):
        product = self.find(loc.product_loc).nth(item_number)
        product.click()

    def add_to_compare(self, item_number: int):
        self.page.wait_for_selector(loc.product_loc, timeout=5000)
        self.find(loc.product_loc).nth(item_number).hover()
        add_to_compare_button = self.page.locator(
            loc.add_to_compare_loc
        ).nth(item_number)
        expect(add_to_compare_button).to_be_visible(timeout=5000)
        add_to_compare_button.click()

    def check_item_is_added_to_compare(self):
        self.page.wait_for_selector(loc.compare_section_loc, timeout=5000)
        product_in_compare = self.page.locator(loc.product_in_compare_loc)
        expect(product_in_compare).not_to_be_empty()

    def hover_over_product_card(self, product_card_number: int):
        self.page.wait_for_selector(loc.product_loc, timeout=5000)
        self.find(loc.product_loc).nth(product_card_number).hover()

    def choose_product_size(self, product_card_number: int, size_nth: int):
        product_card = self.find(loc.product_loc).nth(product_card_number)
        size_locator = product_card.locator(loc.product_size_loc)
        size_locator.nth(size_nth).click()

    def choose_product_color(self, product_card_number: int, color_nth: int):
        product_card = self.find(loc.product_loc).nth(product_card_number)
        color_locator = product_card.locator(loc.product_color_loc)
        color_locator.nth(color_nth).click()

    def click_add_to_cart_button(self, product_card_number: int):
        product_card = self.find(loc.product_loc).nth(product_card_number)
        add_to_cart_button_locator = product_card.locator(loc.add_to_cart_button_loc)
        add_to_cart_button_locator.click()

    def check_item_is_added_to_cart(self):
        self.page.wait_for_selector(loc.not_empty_cart_icon_loc, timeout=5000)
        cart_icon_locator = self.find(loc.not_empty_cart_icon_loc)
        expect(cart_icon_locator).to_have_text('1', timeout=5000)
