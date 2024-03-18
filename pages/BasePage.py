import logging
import os.path

import allure
from selenium.webdriver import ActionChains

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


class BasePage:

    TIMEOUT = 5.0
    PAUSE = 0.1

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step("Клик по элементу на странице")
    def click(self, locator):
        self.logger.info(f"Check if element {locator} is present and click")
        ActionChains(self.browser).move_to_element(locator).pause(self.PAUSE).click().perform()

    @allure.step("Ввод символов с клавиатуры")
    def send_keys(self, locator: tuple, keys):
        self.logger.info(f"checking to send characters to {locator}")
        element = self.element(locator)
        element.send_keys(locator, keys)

    @allure.step("Скриншот для разбора")
    def save_screenshot(self):
        self.logger.info(f"Saving screenshot")
        index = 0
        os.makedirs("screenshots", exist_ok=True)
        while os.path.exists(f"screenshots/{index}.png"):
            index += 1
        self.browser.get_screenshot_as_file(f"screenshots/{index}.png")

    @allure.step("Нахождение элемента на странице")
    def element(self, locator: tuple):
        try:
            WebDriverWait(self.browser, self.TIMEOUT).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            print("URL in error:", self.browser.url)
            print("URL in error2:", self.browser.current_url)
            logger.exception(e)
            allure.attach(
                name="Screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            self.save_screenshot()
            raise AssertionError(f"Element is not visible {locator}")

    @allure.step("Нахождение элементов на странице")
    def elements(self, locator: tuple):
        try:
            WebDriverWait(self.browser, self.TIMEOUT).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element is not visible {locator}")

    @allure.step("Ввод текста в поле")
    def _fill_input_field(self, field, text):
        self.logger.info(f"Input {text} in input {field}")
        field = self.element(field)
        field.click()
        field.clear()
        field.send_keys(text)