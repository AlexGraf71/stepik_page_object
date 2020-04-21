from .base_page import BasePage
from .locators import ProductLocators


class ProductPage(BasePage):

    def click_for_basket(self):
        basket = self.browser.find_element(*ProductLocators.ADD_TO_BASKET)
        basket.click()

    def should_be_product_url(self):
        assert 'catalogue' in self.browser.current_url, "Wrong url"

    def should_be_basket_are_present(self):
        assert self.is_element_present(*ProductLocators.ADD_TO_BASKET), "Basket not are present"

    def should_be_product_page(self):
        self.should_be_basket_are_present()
        self.should_be_product_url()
