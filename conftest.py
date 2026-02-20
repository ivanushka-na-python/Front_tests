import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep



@pytest.fixture
def mobile_driver():
    options = Options()
    options.add_argument('--window-size=450,900')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    sleep(4)
    chrome_driver.quit()

@pytest.fixture
def desktop_driver():
    options = Options()
    options.add_argument('--window-size=1440,900')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    sleep(4)
    chrome_driver.quit()
    
