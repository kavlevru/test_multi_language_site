from selenium.webdriver.common.by import By
import time

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_search_add_cart_button(browser):
    browser.get(url)
    time.sleep(30)
