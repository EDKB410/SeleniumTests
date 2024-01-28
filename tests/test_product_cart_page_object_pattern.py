import allure

from pages.ProductCardPage import ProductCardPage


@allure.title("Тест страницы товара")
def test_product_card_page(browser):
    ProductCardPage(browser).check_elements_on_page()
@allure.title("Тест малого радио-баттон")
def test_small_radio_button(browser):
    ProductCardPage(browser).check_small_radio()