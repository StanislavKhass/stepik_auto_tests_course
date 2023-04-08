import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_cart(browser):
    browser.get(link)
    time.sleep(30)

    try:
        cart_button = browser.find_element(By.CSS_SELECTOR, "div.content div#content_inner div.row div.product_main > form button.btn-add-to-basket")
    except NoSuchElementException:
        assert False , "Error: NoSuchElement"
    else:
        assert True
