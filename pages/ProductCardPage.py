import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductCardPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h3")
    PRODUCT_DETAILS_LIST = (By.CSS_SELECTOR, ".list-unstyled")
    SMALL_RADIO = (By.CSS_SELECTOR, "input[type='radio'][name='option[218]'][value='5']")
    MEDIUM_RADIO = (By.CSS_SELECTOR, "input[type='radio'][name='option[218]'][value='6']")
    LARGE_RADIO = (By.CSS_SELECTOR, "input[type='radio'][name='option[218]'][value='7']")
    FIRST_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='8']")
    SECOND_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='9']")
    THIRD_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='10']")
    FORTH_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='11']")
    TEXT_INPUT = (By.CSS_SELECTOR, "#input-option208")

    def __init__(self, driver):
        super().__init__(driver)
        with allure.step(f"Открывается страница браузера"):
            self.browser.get(self.browser.url + "/en-gb/product/apple-cinema")

    @allure.step("Проверить элементы страницы")
    def check_elements_on_page(self):
        self.element(self.HEADER)
        self.element(self.SMALL_RADIO)
        self.element(self.MEDIUM_RADIO)
        self.element(self.LARGE_RADIO)

    @allure.step("Проверка радио-баттон")
    def check_small_radio(self):
        self.element(self.SMALL_RADIO).click()

    @allure.step("Проверка радио-баттон")
    def check_medium_radio(self):
        self.element(self.MEDIUM_RADIO).click()

    @allure.step("Проверка радио-баттон")
    def check_large_radio(self):
        self.element(self.LARGE_RADIO).click()