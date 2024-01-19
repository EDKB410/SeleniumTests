import time

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
        self.browser.get(self.browser.url + "/administration")

    def check_elements_on_page(self):
        self.element(self.USERNAME_INPUT)
        self.element(self.PASSWORD_INPUT)
        self.element(self.SUBMIT_BUTTON)
        self.element(self.OPENCART_LINK)
        self.element(self.FORGOTTEN_PASSWORD)

    def administration_login(self):
        self.send_keys(self.USERNAME_INPUT, self.USERNAME)
        self.send_keys(self.PASSWORD_INPUT, self.PASSWORD)
        self.click(self.SUBMIT_BUTTON)
        self.element(self.OPENCART_LINK)

    def administration_logout(self):
        self.click(self.BUTTON_LOGOUT)
        self.element(self.LOGIN_FORM)






    # LOGIN_SUCCESS = (By.LINK_TEXT, "logout")
    # PERCENT_ORDERS = (By.XPATH, "//*[text()='Total Orders ']/span[@class='float-end']")
    # PERCENT_SALES = (By.XPATH, "//*[text()='Total Sales ']/span[@class='float-end']")
    # PERCENT_CUSTOMERS = (By.XPATH, "//*[text()='Total Customers ']/span[@class='float-end']")
    # PERSON_LABEL = (By.XPATH, "//span[@class='d-none d-md-inline d-lg-inline']")
    # UNSUCCESSIBLE_LOGIN_ALERT = (By.XPATH, "//*[@class='alert alert-danger alert-dismissible']")
    # UNSUCCESSIBLE_LOGIN_TEXT = (By.XPATH, "//i[@class='fa-solid fa-circle-exclamation']")
    # CUSTOMERS_MENU = (By.XPATH, "//*[@class='fas fa-user']")
    # CUSTOMERS = (By.XPATH, "// a[text() = 'Customers']")
    # SELECT_ALL_USERS = (By.XPATH, "//thead//input[@class='form-check-input']")
    # TRASH_ALL_USERS = (By.XPATH, "//*[@class='fa-regular fa-trash-can']")

    #     wait.until(EC.visibility_of_element_located(LoginAdminPage.UNSUCCESSIBLE_LOGIN_ALERT))
    #     message = browser.find_element(*LoginAdminPage.UNSUCCESSIBLE_LOGIN_ALERT).text
    #     assert_message = "No match for Username and/or Password."
    #     assert message == assert_message, "Некорректное сообщение об ошибке"

    # PANEL_TITLE = (By.CSS_SELECTOR, "h1.panel-title")
    # USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    # PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    # SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    # OPENCART_LINK = (By.CSS_SELECTOR, "#footer > a")
    # FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    #
    # USERNAME = "user"
    # PASSWORD = "bitnami"
    #
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.browser.get(self.browser.url + "/admin")
    #
    # def check_elements_on_page(self):
    #     self.element(self.PANEL_TITLE)
    #     self.element(self.USERNAME_INPUT)
    #     self.element(self.PASSWORD_INPUT)
    #     self.element(self.SUBMIT_BUTTON)
    #     self.element(self.OPENCART_LINK)
    #     self.element(self.FORGOTTEN_PASSWORD)
    #
    # def login_as_admin(self):
    #     self._send_keys(self.USERNAME_INPUT, self.USERNAME)
    #     self._send_keys(self.PASSWORD_INPUT, self.PASSWORD)
    #     self.element(self.SUBMIT_BUTTON).click()