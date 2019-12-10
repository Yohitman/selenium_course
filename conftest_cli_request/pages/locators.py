from selenium.webdriver.common.by import By

class main_page_locators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class login_page_locators():
    LOGIN_URL = "login/"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
