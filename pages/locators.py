from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.TAG_NAME, "h1")
    PRICE_PRODUCT = (By.CLASS_NAME, "price_color")
    NAME_PRODUCT_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    #PRICE_PRODUCT_IN_BASKET = (By.XPATH, '/ html / body / div[2] / div / div[1] / div[3] / div / p[1] / strong')
    PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.col-sm-6>.price_color')


