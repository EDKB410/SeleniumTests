import allure
from selenium.webdriver.common.by import By

import helpers
from pages.BasePage import BasePage


class RegistrationPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h1")
    ACCOUNT_LEGEND = (By.CSS_SELECTOR, "#account > legend")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    NEWSLETTER_RADIO_YES = (By.CSS_SELECTOR, "input[type='checkbox'][name='newsletter'][value='1']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][name='agree']")
    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, "a>b")

    SUCCESS_MESSAGE_HEADER = (By.CSS_SELECTOR, "#content > h1")
    SUCCESS_MESSAGE_PARAGRAPH = (By.CSS_SELECTOR, "#content > p")

    def __init__(self, driver):
        super().__init__(driver)
        with allure.step(f"Открывается страница браузера"):
            self.browser.get(self.browser.url + "/index.php?route=account/register")

    @allure.step("Проверка элементов на странице ")
    def check_elements_on_page(self):
        self.element(self.HEADER)
        self.element(self.ACCOUNT_LEGEND)
        self.element(self.FIRSTNAME_INPUT)
        self.element(self.LASTNAME_INPUT)
        self.element(self.EMAIL_INPUT)
        self.element(self.PASSWORD_INPUT)
        self.element(self.NEWSLETTER_RADIO_YES)
        self.element(self.SUBMIT_BUTTON)
        self.element(self.PRIVACY_POLICY_CHECKBOX)
        self.element(self.PRIVACY_POLICY_LINK)

    @allure.step("Заполнить все поля")
    def input_all_fields(self):
        user_first_name = helpers.random_string(5)
        user_last_name = helpers.random_string(5)
        password = helpers.random_string(10)
        self.send_keys(self.FIRSTNAME_INPUT, user_first_name)
        self.send_keys(self.LASTNAME_INPUT, user_last_name)
        self.send_keys(self.EMAIL_INPUT, helpers.random_email())
        self.send_keys(self.PASSWORD_INPUT, password)
        self.element(self.PRIVACY_POLICY_CHECKBOX).click()
        self.element(self.SUBMIT_BUTTON).click()

    @allure.step("Завершение регистрации")
    def check_registration_success(self):
        return self.element(self.SUCCESS_MESSAGE_HEADER) == "Your Account Has Been Created!" and \
               self.element(self.SUCCESS_MESSAGE_PARAGRAPH) == "Congratulations! Your new account has been successfully created!"

    @allure.step("Регистрация нового юзера")
    def register_new_user(self):
        self.input_all_fields()
        self.check_registration_success()