from selenium import webdriver
import time
import math


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
x = browser.find_element_by_id('input_value').text
ans = browser.find_element_by_id('answer')

browser.execute_script("return arguments[0].scrollIntoView(true);", ans)
ans.send_keys(calc(x))

checkb = browser.find_element_by_id('robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", checkb)
checkb.click()

radio = browser.find_element_by_id('robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


