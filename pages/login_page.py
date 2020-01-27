from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()   
    
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGINFORM_LINK), "Login form is not displayed"# реализуйте проверку, что есть форма логина
      
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGFORM_LINK), "Register form is not displayed"# реализуйте проверку, что есть форма регистрации на странице
        
    def should_be_login_url(self):
       # "login" in self.current_url
        assert  "login" in self.browser.current_url, "Login is absent in URL"
        
        
