import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions

from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.options import Options as SafariOptions


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser", default="chrome")
    url = request.config.getoption("--url", default="http://192.168.1.64:8081")

    if browser_name == "chrome":
        service = ChromeService()
        options = ChromeOptions()
        options.add_argument("headless=new")  # Отключение визуализации браузера
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        service = FFService()
        options = FFOptions()
        options.add_argument("-headless")  # Отключение визуализации браузера
        driver = webdriver.Firefox(service=service, options=options)

    else:
        service = SafariService()
        options = SafariOptions()
        options.add_argument("-headless")  # Отключение визуализации браузера
        driver = webdriver.Safari(service=service, options=options)

    # Set window size
    # width = 1920  # in pixels
    # height = 1080  # in pixels
    # driver.set_window_size(width, height)
    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver