from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.elements.ListElement import ListElement


class MainPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "[name='search']")
    CART_BUTTON = (By.CSS_SELECTOR, "#header-cart")
    NAVIGATION_BAR = (By.CSS_SELECTOR, "ul.nav.navbar-nav")
    CONTENT_DIV = (By.CSS_SELECTOR, "#content")
    PARTNERS_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
    EMPTY_SHOPPING_CARD_LABEL = (By.CSS_SELECTOR, "li.text-center")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency > div > a > span")
    CURRENCY_LIST = (By.CSS_SELECTOR, "#form-currency > div > ul")
    CURRENCY_LIST_ITEM = (By.CSS_SELECTOR, "li")

    def change_currency(self, text):
        currency_button = self.element(self.CURRENCY_BUTTON)
        currency_button.click()
        ListElement(self.browser).click_item(text)

    def click_cart_button(self):
        self.element(self.CART_BUTTON).click()

    def check_empty_shopping_card_label(self):
        self.click_cart_button()
        return self.element(self.EMPTY_SHOPPING_CARD_LABEL).text == "Your shopping cart is empty!"