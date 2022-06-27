from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.main_page import MainPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.product_added_to_basket()
    page.solve_quiz_and_get_code()
    page.product_in_basket()
    page.correct_price_in_basket()
