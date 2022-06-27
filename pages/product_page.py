from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import math


class ProductPage(BasePage):
    def product_added_to_basket(self):
        basket_add = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        basket_add.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        product_basket_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text
        assert product_name == product_basket_name, "The product name in the cart is not correct"

    def correct_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        product_price_in_busket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET).text
        assert product_price in product_price_in_busket, "The price of the item in the cart is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD), 'Message is present'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD), 'Message is not disapeared'