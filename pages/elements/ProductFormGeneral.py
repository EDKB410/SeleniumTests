import time

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

import helpers


class ProductFormGeneral(BasePage):
    SELF = (By.CSS_SELECTOR, "tab-general")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name-1")
    # DESCRIPTION_INPUT = (By.XPATH, "//*[@id='cke_1_contents']")
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title-1")
    META_TAG_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "#input-meta-description-1")
    META_TAG_KEYWORD_INPUT = (By.CSS_SELECTOR, "#input-meta-keyword-1")
    PRODUCT_TAGS_INPUT = (By.CSS_SELECTOR, "#input-tag-1")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def fill_in_all_fields(self, product_name):
        self.send_keys(self.PRODUCT_NAME_INPUT, product_name)
        self.send_keys(self.META_TAG_TITLE_INPUT, helpers.random_string(5))
        self.send_keys(self.META_TAG_DESCRIPTION_INPUT, helpers.random_string(5))
        self.send_keys(self.META_TAG_KEYWORD_INPUT, helpers.random_string(5))
        self.send_keys(self.PRODUCT_TAGS_INPUT, helpers.random_string(5))

    def submit_form(self):
        self.fill_in_all_fields()
        self.element(self.SUBMIT_BUTTON).click()