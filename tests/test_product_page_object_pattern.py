from pages.AdminMainPage import AdminMainPage
from pages.AdminLoginPage import AdminLoginPage
from pages.ProductsPage import ProductsPage

PRODUCT_NAME = "Lenovo Think Pad 2.0"


def test_product_creation(browser):
    AdminLoginPage(browser).administration_login()
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser).create_new_product(PRODUCT_NAME)


def test_product_deletion(browser):
    AdminLoginPage(browser).administration_login()
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser).delete_product(PRODUCT_NAME)