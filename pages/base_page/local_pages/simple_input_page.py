from pages.base_page.base_page import BasePage
from selenium.webdriver.common.by import By


"""подумать где нормально хранить локаторы"""
h1_loc = (By.TAG_NAME, 'h1')
h1_text = 'Input field'
text_string_loc = (By.ID, 'id_text_string')
valid_result_element = (By.ID, 'result-text')
invalid_result_element = (By.ID, 'error_1_id_text_string')
invalid_result_text = 'Enter a valid string consisting of letters, numbers, underscores or hyphens.'
invalid_result_1_text = 'Please enter 2 or more characters'
invalid_result_25_text = 'Please enter no more than 25 characters'


class SimpleInputPage(BasePage):

    page_url = '/input/simple'

    def __init__(self, driver):
        super().__init__(driver)


    def check_h1_text(self):
        self.check_result_text(h1_loc, h1_text)


    def send_keys_to_text_input(self, test_data):
        self.send_keys(text_string_loc, test_data)


    def submit_text_input(self):
        self.submit(text_string_loc)


    def check_valid_result_text_input(self, test_data):
        self.check_result_text(valid_result_element, test_data)


    def check_invalid_result_text_input(self):
        self.check_result_text(invalid_result_element, invalid_result_text)


    def check_invalid_1_result_text_input(self):
        self.check_result_text(invalid_result_element, invalid_result_1_text)


    def check_invalid_25_result_text_input(self):
        self.check_result_text(invalid_result_element, invalid_result_25_text)


















    """дописать в классе base_page общие методы, создать по классу на каждую страницу, назначить дочерние классы, 
    выписать локаторы и тестовые данные в отдельные файлы, собрать из всего сами вызовы методов, добавить фикстуры, 
    инициализирующие страницы сайта"""