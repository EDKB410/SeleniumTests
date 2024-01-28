import allure

from pages.AdminLoginPage import AdminLoginPage

@allure.title("Вход выход администратора")
def test_login_logout_administration(browser):
    page = AdminLoginPage(browser)
    page.check_elements_on_page()
    page.administration_login()
    page.administration_logout()