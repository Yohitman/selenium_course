from selenium import webdriver
import os



link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
inputs = browser.find_elements_by_css_selector('input[type="text"]')
for i in inputs:
	i.send_keys("мой ответ")

filesender= browser.find_element_by_css_selector('input[type="file"]')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
filesender.send_keys(file_path)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

