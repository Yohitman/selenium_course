from pages.main_page import main_page
from pages.login_page import login_page

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = main_page(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_invalid_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = main_page(browser, link)
    page.open()
    page.should_be_login_link()

def test_login_page_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = main_page(browser, link)
    page.open()
    page.go_to_login_page()
    login_pages = login_page(browser, browser.current_url)
    login_pages.should_be_login_url()

def test_login_page_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = main_page(browser, link)
    page.open()
    page.go_to_login_page()
    login_pages = login_page(browser, browser.current_url)
    login_pages.should_be_login_form()

def test_login_page_registration_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = main_page(browser, link)
    page.open()
    page.go_to_login_page()
    login_pages = login_page(browser, browser.current_url)
    login_pages.should_be_register_form()
