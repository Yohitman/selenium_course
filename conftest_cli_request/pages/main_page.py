from .base_page import base_page
from selenium.webdriver.common.by import By
from .locators import main_page_locators


class main_page(base_page):
    def go_to_login_page(self):
        link = self.browser.find_element(*main_page_locators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*main_page_locators.LOGIN_LINK), "Login link is not presented"
