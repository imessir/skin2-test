import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

baseurl = "https://opm-website.iot-asm-test1.insitech.live/"


@pytest.fixture(autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(5)
    browser.get(baseurl)
    yield browser
    browser.quit()


def is_element_present(browser, how, what):
    try:
        browser.find_element(how, what)
    except NoSuchElementException:
        return False
    return True


def test_should_be_top_elements(browser):
    element_ids = ["main_logo", "open_city_modal_btn", "shop_address_map_btn", "notifications_btn"]
    for element_id in element_ids:
        assert is_element_present(browser, By.ID, element_id), f"{element_id} element is not presented"
