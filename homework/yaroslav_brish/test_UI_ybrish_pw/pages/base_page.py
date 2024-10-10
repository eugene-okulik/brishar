from playwright.sync_api import Page, expect


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError(
                'Page can not be opened for this page class'
            )

    def find(self, locator):
        return self.page.locator(locator)

    def check_header_text(self, title: str):
        h1_element = self.page.locator('h1')
        expect(h1_element).to_have_text(title)
