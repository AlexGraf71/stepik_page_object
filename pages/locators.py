from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_USERNAME = (By.CSS_SELECTOR, '[name="login-username"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTRATION_PASSWORD_FIRST = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_PASSWORD_SECOND = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_COST = (By.CSS_SELECTOR, '.product_main>p')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRODUCT_COST_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info> div > p:nth-child(1) > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class BasketPageLocators:
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.thumbnail')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner')