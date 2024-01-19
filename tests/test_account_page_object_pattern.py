from pages.RegisteredPage import RegistrationPage


def test_register_account(browser):
    page = RegistrationPage(browser)
    page.check_elements_on_page()
    page.register_new_user()