from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AdminMainPage(BasePage):
    MENU = (By.CSS_SELECTOR, "#menu")
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCT_MENU_ITEM = (By.XPATH, '//*[@id="collapse-1"]/li[2]/a')
    CREATE_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")

    def open_products_page(self):
        self.element(self.CATALOG).click()
        self.element(self.PRODUCT_MENU_ITEM).click()