from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        link_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        link_email.send_keys(email)
        link_password = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        link_password.send_keys(password)
        password1 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        password1.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()
    
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGINFORM_LINK), "Login form is not displayed"
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    def should_be_login_url(self):
        assert  "login" in self.browser.current_url, "Login is absent in URL"
    
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGFORM_LINK), "Register form is not displayed"# реализуйте проверку, что есть форма регистрации на странице
        
    
        
    
