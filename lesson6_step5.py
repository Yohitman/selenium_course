from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
x = browser.find_element_by_id('input_value').text
ans = browser.find_element_by_id('answer')

ans.send_keys(calc(x))

checkb = browser.find_element_by_id('robotCheckbox')
checkb.click()

radio = browser.find_element_by_id('robotsRule')
radio.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

