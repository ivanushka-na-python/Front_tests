from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'https://www.qa-practice.com/elements'
    page_url = None


    def __init__(self, driver: WebDriver):
        self.driver = driver



    def open_page(self, url=None):
        if url is None:
            url = self.page_url
        if url.startswith('http'):
            full_url = url
        else:
            full_url = self.base_url + url
        self.driver.get(full_url)


    '''кароч *locator распаковывает кортеж на состовляющие'''
    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)


    def find_all_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)


    def send_keys(self, locator, keys):
        element = self.find_element(locator)
        element.send_keys(keys)


    def submit(self, locator):
        element = self.find_element(locator)
        element.submit()


    def check_result_text(self, locator, text):
        element = self.find_element(locator)
        assert element.text == text


    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


    def switch_to_main_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])