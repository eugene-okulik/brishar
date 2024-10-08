def test_open_product_page(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.click_on_product_card()
    eco_friendly_page.check_header_text("Ana Running Short")


def test_add_to_compare(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.add_to_compare()
    eco_friendly_page.check_item_is_added_to_compare()


def test_add_to_cart(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.add_to_cart()
    eco_friendly_page.check_item_is_added_to_cart()
