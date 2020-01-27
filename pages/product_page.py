from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADDBUTTON)
        add_button.click()
        
    def should_name_be_same(self):
        assert self.browser.find_element(*ProductPageLocators.NAMETOVARA1).text == self.browser.find_element(*ProductPageLocators.NAMETOVARA2).text, f"The title is different on the page {self.browser.current_url}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def should_price_be_equal(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE1).text == self.browser.find_element(*ProductPageLocators.PRICE2).text, f"The price is different on the page {self.browser.current_url}"  

    def should_success_message_dissappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success Message is presented, but should be dissapered"


    #def test_guest_cant_see_success_message_after_adding_product_to_basket(*ProductPageLocators.SUCCESS_MESSAGE):
       # assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        #        "Success message is presented, but should not be"
            
    #def test_guest_cant_see_success_message(*ProductPageLocators.SUCCESS_MESSAGE):
        #assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        #    "Success message is presented, but should not be"       
            
        
    #def test_message_disappeared_after_adding_product_to_basket(*ProductPageLocators.SUCCESS_MESSAGE):
        #assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        #    "Success Message is presented, but should be dissapered"