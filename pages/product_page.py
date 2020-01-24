from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADDBUTTON)
        add_button.click()
        
    def should_name_be_same(self):
        assert self.browser.find_element(*ProductPageLocators.NAMETOVARA1).text == self.browser.find_element(*ProductPageLocators.NAMETOVARA2).text, "The title is different"
        
    def should_price_be_equal(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE1).text == self.browser.find_element(*ProductPageLocators.PRICE2).text, "The price is different"