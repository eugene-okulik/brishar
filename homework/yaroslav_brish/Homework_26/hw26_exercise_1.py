from playwright.sync_api import Page, expect


def test_form_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username_field = page.get_by_role('textbox', name='username')
    password_field = page.get_by_role('textbox', name='password')
    username_field.fill('tomsmith')
    password_field.fill('SuperSecretPassword!')
    page.get_by_role('button').click()
    welcome_text = page.get_by_role('heading', level=4)
    expect(welcome_text).to_contain_text('Welcome to the Secure Area')
