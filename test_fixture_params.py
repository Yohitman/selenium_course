import time
import math
import pytest

from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["236895/step/1", \
				"236896/step/1", \
				"236897/step/1", \
				"236898/step/1", \
				"236899/step/1", \
				"236903/step/1", \
				"236904/step/1", \
				"236905/step/1"])
def test_guest_should_see_login_link(browser, url):
	link = "https://stepik.org/lesson/{}/".format(url)
	browser.get(link)
	time.sleep(3)
	field = browser.find_element_by_css_selector(".textarea")
	answer = str(math.log(int(time.time())))
	field.send_keys(answer)
	button = browser.find_element_by_css_selector("button.submit-submission")
	button.click()
	time.sleep(3)
	alert_text = browser.find_element_by_css_selector('.smart-hints__hint').text
	assert "Correct!" == alert_text
