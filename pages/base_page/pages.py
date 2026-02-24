from selenium.webdriver import Keys

from conftest import driver


class PageInput:
    def __init__(self, driver, page_url):
        self.driver = driver
        self.page_url = 'https://www.qa-practice.com/elements/input/' + page_url
        self.element = None


    def open_page(self):
        self.driver.get(self.page_url)


    def find_element(self, by, value):
        self.element = self.driver.find_element(by, value)


    def entered_end_submit_field(self, keys):
        self.element.send_keys(keys)
        self.element.submit()


    def check_result(self, result):
        result_text = self.element.text
        assert result_text == result


    # def browser_validate(self, script):
    #     self.element = self.driver.execute_script(script)