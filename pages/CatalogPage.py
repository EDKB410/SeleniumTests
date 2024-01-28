import time

import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CatalogPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h3")
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#button-list")
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#button-grid")
    COMPARE_TOTAL_LINK = (By.CSS_SELECTOR, "#compare-total")
    SORT_INPUT = (By.CSS_SELECTOR, "#input-sort")
    LIMIT_INPUT = (By.CSS_SELECTOR, "#input-limit")

    def __init__(self, driver):
        super().__init__(driver)
        with allure.step(f"Открывается страница браузера"):
            self.browser.get(self.browser.url + "/index.php?route=product/category&path=20")

    @allure.step("Проверить элементы страницы каталога")
    def check_elements_on_page(self):
        self.element(self.HEADER)
        self.element(self.LIST_VIEW_BUTTON)
        self.element(self.GRID_VIEW_BUTTON)
        self.element(self.COMPARE_TOTAL_LINK)
        self.element(self.SORT_INPUT)
        self.element(self.LIMIT_INPUT)