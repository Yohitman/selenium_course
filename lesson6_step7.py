from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1").text
num2 = browser.find_element_by_id("num2").text
i = int(num1) + int(num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(str(i))

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

