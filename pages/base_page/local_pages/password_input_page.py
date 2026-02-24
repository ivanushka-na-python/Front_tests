from pages.base_page.base_page import BasePage
from selenium.webdriver.common.by import By

h1_loc = (By.TAG_NAME, 'h1')
h1_text =  'Input field'
passwd_input_loc = (By.ID, 'id_password')
valid_result_element = (By.ID, 'result-text')
invalid_result_element = (By.ID, 'error_1_id_password')
invalid_result_text = 'Low password complexity'


class PasswordInputPage(BasePage):

    page_url = '/input/passwd'

    def __init__(self, driver):
        super().__init__(driver)


    def check_h1_text(self):
        self.check_result_text(h1_loc, h1_text)


    def send_keys_to_passwd_input(self, test_data):
        self.send_keys(passwd_input_loc, test_data)


    def submit_passwd_input(self):
        self.submit(passwd_input_loc)


    def check_valid_result_passwd_input(self, test_data):
        self.check_result_text(valid_result_element, test_data)


    def check_invalid_result_passwd_input(self):
        self.check_result_text(invalid_result_element, invalid_result_text)
