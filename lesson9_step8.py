from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
waiting = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )
browser.find_element_by_id("book").click()
# Ваш код, который заполняет обязательные поля
x = browser.find_element_by_id('input_value').text
ans = browser.find_element_by_id('answer')

ans.send_keys(calc(x))

# Отправляем заполненную форму
button = browser.find_element_by_css_selector('button.btn[id="solve"]')
button.click()

