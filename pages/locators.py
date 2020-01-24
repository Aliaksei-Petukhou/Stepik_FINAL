from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGFORM_LINK = (By.CSS_SELECTOR, "#register_form1")
    LOGINFORM_LINK = (By.CSS_SELECTOR, "#login_form")