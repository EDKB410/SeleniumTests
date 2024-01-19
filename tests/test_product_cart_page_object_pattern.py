from pages.ProductCardPage import ProductCardPage


def test_product_card_page(browser):
    ProductCardPage(browser).check_elements_on_page()

def test_small_radio_button(browser):
    ProductCardPage(browser).check_small_radio()