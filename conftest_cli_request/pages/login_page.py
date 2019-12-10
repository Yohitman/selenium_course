from .base_page import base_page
from .locators import login_page_locators


class login_page(base_page):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.endswith(login_page_locators.LOGIN_URL), "Login URL is invalid"

    def should_be_login_form(self):
        assert self.is_element_present(*login_page_locators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*login_page_locators.REGISTRATION_FORM), "Registration form is not presented"
