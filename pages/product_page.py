from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADDBUTTON)
        add_button.click()
        
    def should_name_be_same(self):
        
        
        #if self.browser.find_element(*ProductPageLocators.NAMETOVARA1).text != self.browser.find_element(*ProductPageLocators.NAMETOVARA2).text:
            #curbr = self.browser.current_url
            #print (self.browser.current_url)
        assert self.browser.find_element(*ProductPageLocators.NAMETOVARA1).text == self.browser.find_element(*ProductPageLocators.NAMETOVARA2).text, f"The title is different on the page {self.browser.current_url}"
        
    def should_price_be_equal(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE1).text == self.browser.find_element(*ProductPageLocators.PRICE2).text, f"The price is different on the page {self.browser.current_url}"
