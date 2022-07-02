from selenium.webdriver.common.by import By
import time

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_search_add_cart_button(browser):
    # Given: link to the site 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    # When: I open link in the browser
    # Then: I see the add to cart button on the page
    browser.get(url)

    # Задержка для оценки работы аргумента --language переданного при запуске скрипта
    time.sleep(30)

    button_add = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button_add != [], "The 'add to cart' button was not found on the page"
