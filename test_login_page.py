from .pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


def test_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_registration_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


def test_login_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
