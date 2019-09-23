from selenium import webdriver
import time
import unittest

# Ваш код, который заполняет обязательные поля
class testUNIT(unittest.TestCase):
	def test_reg1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		reqd1 = browser.find_element_by_css_selector('input[required].first')
		reqd2 = browser.find_element_by_css_selector('input[required].second')
		reqd3 = browser.find_element_by_css_selector('input[required].third')
		for i in [reqd1, reqd2, reqd3]:
			i.send_keys("мой ответ")

		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Не туда зарегались(")
	def test_reg2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		reqd1 = browser.find_element_by_css_selector('input[required].first')
		reqd2 = browser.find_element_by_css_selector('input[required].second')
		reqd3 = browser.find_element_by_css_selector('input[required].third')
		for i in [reqd1, reqd2, reqd3]:
			i.send_keys("мой ответ")

		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Не туда зарегались(")

if __name__ == "__main__":
    unittest.main()

