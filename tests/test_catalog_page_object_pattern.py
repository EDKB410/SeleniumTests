import allure

from pages.CatalogPage import CatalogPage


@allure.title("Тест страницы каталог")
def test_catalog_page(browser):
    CatalogPage(browser).check_elements_on_page()