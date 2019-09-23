from selenium import webdriver
import time
import math


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
num1 = browser.find_element_by_id("num1").text
num2 = browser.find_element_by_id("num2").text
x = str(int(num1) + int(num2))

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(x)

button = browser.find_element_by_tag_name("button")
button.click()


