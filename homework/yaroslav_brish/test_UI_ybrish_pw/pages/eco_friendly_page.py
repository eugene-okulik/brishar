from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from playwright.sync_api import expect


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def click_on_product_card(self):
        product = self.find(loc.product_loc)
        product.click()

    def add_to_compare(self):
        self.page.wait_for_selector(loc.product_loc, timeout=5000)
        self.page.hover(loc.product_loc)
        add_to_compare_button = self.page.locator(
            loc.add_to_compare_loc
        )
        expect(add_to_compare_button).to_be_visible(timeout=5000)
        add_to_compare_button.click()

    def check_item_is_added_to_compare(self):
        self.page.wait_for_selector(loc.compare_section_loc, timeout=5000)
        product_in_compare = self.page.locator(loc.product_in_compare_loc)
        expect(product_in_compare).not_to_be_empty()

    def add_to_cart(self):
        self.page.wait_for_selector(loc.product_loc, timeout=5000)
        first_product = self.find(loc.product_loc)
        self.page.wait_for_selector(loc.product_size_loc, timeout=5000)
        product_size = self.find(loc.product_size_loc)
        self.page.wait_for_selector(loc.product_color_loc, timeout=5000)
        product_color = self.find(loc.product_color_loc)
        self.page.wait_for_selector(loc.add_to_cart_button_loc, timeout=5000)
        add_to_cart_button = self.find(loc.add_to_cart_button_loc)
        first_product.hover()
        product_size.click()
        product_color.click()
        add_to_cart_button.click()

    def check_item_is_added_to_cart(self):
        cart_icon_locator = self.find(loc.not_empty_cart_icon_loc)
        expect(cart_icon_locator).to_have_text('1', timeout=5000)
