import allure

from pages.RegisteredPage import RegistrationPage


@allure.title("Регистрация нового аккаунта")
def test_register_account(browser):
    page = RegistrationPage(browser)
    page.check_elements_on_page()
    page.register_new_user()