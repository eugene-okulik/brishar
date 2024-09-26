from playwright.sync_api import Page, expect


def test_alert_click(page: Page):
    page.on("dialog", lambda dialog: dialog.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('.a-button').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_contain_text('Ok')
