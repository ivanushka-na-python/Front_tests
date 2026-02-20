import pytest
from selenium.webdriver.common.by import By



class MobileTest:


    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        
    def select_text_field(self):
        text_string = self.driver.find_element(By.ID, 'id_text_string')
        text_string.send_keys('test')
        text_string.submit()

    def result_text(self):    
        return self.driver.find_element(By.ID, 'result-text')


    def check_text_field(self):
        assert self.result_text().text == 'test'

