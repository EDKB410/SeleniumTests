import allure

from pages.MainPage import MainPage


@allure.title("Проверка пустой страницы корзины")
def test_check_empty_shopping_card_label(browser):
    MainPage(browser).check_empty_shopping_card_label()

@allure.title("Проверка смены валюты")
def test_change_currency(browser):
    MainPage(browser).change_currency("$ US Dollar")