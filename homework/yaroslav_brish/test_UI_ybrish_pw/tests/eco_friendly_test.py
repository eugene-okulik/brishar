def test_open_product_page(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.click_on_product_card(0)
    eco_friendly_page.check_header_text("Ana Running Short")


def test_add_to_compare(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.add_to_compare(1)
    eco_friendly_page.check_item_is_added_to_compare()


def test_add_to_cart(eco_friendly_page):
    eco_friendly_page.open_page()
    product_card_number = 1
    eco_friendly_page.hover_over_product_card(product_card_number)
    eco_friendly_page.choose_product_size(product_card_number, 2)
    eco_friendly_page.choose_product_color(product_card_number, 1)
    eco_friendly_page.click_add_to_cart_button(product_card_number)
    eco_friendly_page.check_item_is_added_to_cart()
