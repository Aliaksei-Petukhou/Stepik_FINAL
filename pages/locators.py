from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGFORM_LINK = (By.CSS_SELECTOR, "#register_form")
    LOGINFORM_LINK = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADDBUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAMETOVARA1 = (By.CSS_SELECTOR, ".alertinner strong")
    NAMETOVARA2 = (By.CSS_SELECTOR, ".product_main h1 ")
    PRICE1 = (By.CSS_SELECTOR, ".alert-info strong")
    PRICE2 = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE =( By.CSS_SELECTOR, ".alertinner")

