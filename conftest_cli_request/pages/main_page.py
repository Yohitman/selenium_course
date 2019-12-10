from .base_page import base_page
from selenium.webdriver.common.by import By

class main_page(base_page):
#    def go_to_login_page(self):
#        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
