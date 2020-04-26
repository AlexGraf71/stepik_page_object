from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        self.should_not_be_to_basket()
        self.should_not_be_message()

    def should_not_be_to_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            'The product is in the basket, but should not be'

    def should_not_be_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), \
            'The message should be, but it is not'
