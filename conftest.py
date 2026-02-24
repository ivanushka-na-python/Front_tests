import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.base_page.local_pages.simple_input_page import SimpleInputPage
from pages.base_page.local_pages.email_input_page import EmailInputPage
from pages.base_page.local_pages.password_input_page import PasswordInputPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1440,900')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def simple_input_page(driver):
    return SimpleInputPage(driver)

@pytest.fixture
def email_input_page(driver):
    return EmailInputPage(driver)

@pytest.fixture
def password_input_page(driver):
    return PasswordInputPage(driver)