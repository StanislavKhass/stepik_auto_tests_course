
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time
from selenium.webdriver.common.by import By

def test_check_button_cart(browser):
    browser.get(link)
    time.sleep(30)
    cart_button = browser.find_element(By.CSS_SELECTOR, "div.content div#content_inner div.row div.product_main form button")
    assert cart_button , "Ошибка: Кнопка не существует"
