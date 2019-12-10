from pages.main_page import main_page

#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = main_page(browser, link)
#    page.open()
#    page.go_to_login_page()

def test_guest_should_see_invalid_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = main_page(browser, link)
    page.open()
    page.should_be_login_link()