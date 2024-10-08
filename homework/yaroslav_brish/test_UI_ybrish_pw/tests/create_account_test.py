def test_create_account_with_existing_email(create_account_page):
    create_account_page.open_page()
    create_account_page.enter_first_name('test')
    create_account_page.enter_last_name('test')
    create_account_page.enter_email('test@test.com')
    create_account_page.enter_password('Test@123')
    create_account_page.confirm_password('Test@123')
    create_account_page.click_button()
    create_account_page.check_alert_appears()


def test_weak_password(create_account_page):
    create_account_page.open_page()
    create_account_page.enter_first_name('test')
    create_account_page.enter_last_name('test')
    create_account_page.enter_email('test@test.com')
    create_account_page.check_password_is_weak('qwerty')


def test_check_header_text(create_account_page):
    create_account_page.open_page()
    create_account_page.check_header_text("Create New Customer Account")
