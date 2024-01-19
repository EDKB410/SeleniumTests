import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from pages.BasePage import BasePage
from pages.elements.ProductFormGeneral import ProductFormGeneral
from pages.elements.ProductFormData import ProductFormData
from pages.elements.FilterForm import FilterForm


class ProductsPage(BasePage):
    CREATE_NEW_PRODUCT_BUTTON = (By.XPATH, "//div[@class='float-end']/a[@class='btn btn-primary']")
    SAVE_PRODUCT_BUTTON = (By.XPATH, "//*[@class='float-end']/button[1]")
    COPY_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Copy']")
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button.btn-danger")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
    NAV_TAB_GENERAL = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(1) > a")
    NAV_TAB_DATA = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a")
    PRODUCT_FORM = (By.CSS_SELECTOR, "#form-product")
    SELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, 'input[type=checkbox]')

    def click_add_new_product_button(self):
        self.element(self.CREATE_NEW_PRODUCT_BUTTON).click()

    def click_save_product_button(self):
        self.element(self.SAVE_PRODUCT_BUTTON).click()

    def click_nav_tab_data(self):
        self.element(self.NAV_TAB_DATA).click()

    def check_success_message(self):
        return self.element(self.SUCCESS_MESSAGE).text == "Success: You have modified products!"

    def create_new_product(self, product_name):
        self.click_add_new_product_button()
        ProductFormGeneral(self.browser).fill_in_all_fields(product_name)
        self.click_nav_tab_data()
        ProductFormData(self.browser).fill_in_all_fields()
        self.click_save_product_button()
        self.check_success_message()

    def delete_product(self, product_name):
        FilterForm(self.browser).filter_product_by_name(product_name)
        time.sleep(1)
        self.element(self.SELECT_ALL_CHECKBOX).click()
        self.element(self.DELETE_PRODUCT_BUTTON).click()
        Alert(self.browser).accept()
        self.check_success_message()