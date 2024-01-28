import time

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

import helpers


class ProductFormData(BasePage):
    PRODUCT_MODEL_INPUT = (By.XPATH, "//input[@name='model']")
    SEO = (By.XPATH, "//a[@href='#tab-seo']")
    SEO_KEYWORD = (By.XPATH, "//table/tbody//input[@name='product_seo_url[0][1]']")

    def fill_in_all_fields(self):
        self._send_keys(self.PRODUCT_MODEL_INPUT, helpers.random_string(5))
        self.element(self.SEO).click()
        self._send_keys(self.SEO_KEYWORD, helpers.random_string(5).upper())