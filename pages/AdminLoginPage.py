import time

import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BUTTON_LOGOUT = (By.XPATH, "//span[@class='d-none d-md-inline']")
    LOGIN_FORM = (By.XPATH, "//div[@class='card-header']")

    USERNAME = "user"
    PASSWORD = "bitnami"

    def __init__(self, driver):
        super().__init__(driver)
        with allure.step(f"Открывается страница браузера"):
            self.browser.get(self.browser.url + "/administration")

    @allure.step("Нахождение элементов на странице")
    def check_elements_on_page(self):
        self.element(self.USERNAME_INPUT)
        self.element(self.PASSWORD_INPUT)
        self.element(self.SUBMIT_BUTTON)
        self.element(self.OPENCART_LINK)
        self.element(self.FORGOTTEN_PASSWORD)

    @allure.step("Логин под учеткой администратора")
    def administration_login(self):
        self._send_keys(self.USERNAME_INPUT, self.USERNAME)
        self._send_keys(self.PASSWORD_INPUT, self.PASSWORD)
        self.element(self.SUBMIT_BUTTON).click()
        self.element(self.OPENCART_LINK)

    @allure.step("Разлогин из под учетки администратора")
    def administration_logout(self):
        self.element(self.BUTTON_LOGOUT).click()
        self.element(self.LOGIN_FORM)