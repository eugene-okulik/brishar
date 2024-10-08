from pages.base_page import BasePage
from pages.locators import sale_locators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def women_sale(self):
        self.page.wait_for_selector(loc.women_sale_loc, timeout=5000)
        women_sale = self.find(loc.women_sale_loc)
        women_sale.click()

    def men_sale(self):
        self.page.wait_for_selector(loc.men_sale_loc, timeout=5000)
        men_sale = self.find(loc.men_sale_loc)
        men_sale.click()

    def gear(self):
        self.page.wait_for_selector(loc.gear_loc, timeout=5000)
        gear = self.find(loc.gear_loc)
        gear.click()
