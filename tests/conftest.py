import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions

from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.options import Options as SafariOptions
from utils import setup_logging

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    try:
        if rep.when == 'call' and rep.failed:
            if 'browser' in item.fixturenames:
                web_driver = item.funcargs['browser']
            else:
                print('Fail to take screen-shot')
                return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        print('Fail to take screen-shot: {}'.format(e))

def driver_factory(request):
    browser_name = request.config.getoption("--browser", default="chrome")

    executor = request.config.getoption("--executor", default="local")

    if executor == "local":
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

        elif browser_name == "safari":
            service = SafariService()
            options = SafariOptions()
            options.add_argument("-headless")  # Отключение визуализации браузера
            driver = webdriver.Safari(service=service, options=options)
        else:
            raise Exception("Driver not supported")
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        moon_options = {
            "enableVNC": True,
            "enableVideo": True,
            "name": f"SetupUser",
            "sessionTimeout": "5m"
        }
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "120.0")
        options.set_capability("moon:options", moon_options)
        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options)
    return driver

@pytest.fixture
def browser(request):
    url = request.config.getoption("--url", default="http://192.168.1.64:8081")
    log_level = request.config.getoption("--log_level", default="INFO")
    test_name = request.node.name

    logger = setup_logging(log_level, test_name)
    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))

    driver = driver_factory(request)
    driver.maximize_window()
    driver.test_name = test_name
    driver.log_level = log_level
    driver.url = url
    driver.logger = logger

    logger.info("Browser: {}".format(driver.capabilities))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver