from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage): 

    def should_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRICEBASKET), "Basket is not empty , but should be"
        
    def should_be_text_about_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMTY), "Basket is not empty, text about it is absent"# реализуйте проверку, что есть форма логина