from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_search_add_cart_button(browser):
    browser.get(url)
