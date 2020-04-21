from .base_page import BasePage
from .locators import ProductLocators


class ProductPage(BasePage):

    def click_for_basket(self):
        basket = self.browser.find_element(*ProductLocators.ADD_TO_BASKET)
        basket.click()

    def should_be_product_page(self):
        self.should_be_basket_are_present()
        self.should_be_product_url()
        self.should_be_name_product()
        self.should_be_cost_product()

    def should_be_product_url(self):
        assert 'catalogue' in self.browser.current_url, "Wrong url"

    def should_be_basket_are_present(self):
        assert self.is_element_present(*ProductLocators.ADD_TO_BASKET), "Basket not are present"

    def should_be_name_product(self):
        assert self.browser.find_element(*ProductLocators.PRODUCT_NAME).text == self.browser.find_element \
            (*ProductLocators.PRODUCT_NAME_IN_MESSAGE).text, 'Wrong product name'

    def should_be_cost_product(self):
        assert self.browser.find_element(*ProductLocators.PRODUCT_COST).text == self.browser.find_element \
            (*ProductLocators.PRODUCT_COST_IN_MESSAGE).text, 'Wrong product cost'
