from playwright.sync_api import Page, expect


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    # clickable_button = page.locator('#enableAfter')
    # expect(clickable_button).to_be_enabled()
    color_button = page.locator('#colorChange')
    expect(color_button).to_have_css('color', 'rgb(220, 53, 69)')
    color_button.click()
    expect(color_button).to_be_focused()
