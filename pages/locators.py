from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_USERNAME = (By.CSS_SELECTOR, '[name="login-username"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTRATION_PASSWORD_FIRST = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_PASSWORD_SECOND = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')