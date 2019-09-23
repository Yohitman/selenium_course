from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

# Ваш код, который заполняет обязательные поля
x = browser.find_element_by_id('input_value').text
ans = browser.find_element_by_id('answer')

ans.send_keys(calc(x))

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

