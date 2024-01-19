from pages.CatalogPage import CatalogPage


def test_catalog_page(browser):
    CatalogPage(browser).check_elements_on_page()