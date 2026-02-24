import  pytest
from pages.base_page.pages import PageInput
from selenium.webdriver.common.by import By
from data.test_data_imputs import validPayloadSimple as validDataSimple
from data.test_data_imputs import invalidPayloadSimple as invalidDataSimple
from data.test_data_imputs import invalid1PayloadSimple as invalid1DataSimple
from data.test_data_imputs import invalid25PayloadSimple as invalid25DataSimple
from data.test_data_imputs import validPayloadEmail as validDataEmail
from data.test_data_imputs import invalidPayloadEmail as invalidDataEmail
from data.test_data_imputs import validPayloadPassword as validDataPassword
from data.test_data_imputs import invalidPayloadPassword as invalidDataPassword




'''TestSimpleInput'''
@pytest.mark.parametrize('payload', validDataSimple)
def test_valid_text_input(driver, payload):
    page_input = PageInput(driver, 'simple')
    page_input.open_page()
    page_input.find_element(By.ID, 'id_text_string')
    page_input.entered_end_submit_field(payload)
    page_input.find_element(By.ID, 'result-text')
    page_input.check_result(payload)


@pytest.mark.parametrize('payload', invalidDataSimple)
def test_invalid_text_input(driver, payload):
    page_input = PageInput(driver, 'simple')
    page_input.open_page()
    page_input.find_element(By.ID, 'id_text_string')
    page_input.entered_end_submit_field(payload)
    page_input.find_element(By.ID, 'error_1_id_text_string')
    page_input.check_result(
        'Enter a valid string consisting of letters, numbers, underscores or hyphens.'
    )

@pytest.mark.parametrize('payload', invalid1DataSimple)
def test_one_symbols_text_input(driver, payload):
    page_input = PageInput(driver, 'simple')
    page_input.open_page()
    page_input.find_element(By.ID, 'id_text_string')
    page_input.entered_end_submit_field(payload)
    page_input.find_element(By.ID, 'error_1_id_text_string')
    page_input.check_result(
        'Please enter 2 or more characters'
    )

@pytest.mark.parametrize('payload', invalid25DataSimple)
def test_more_then_25_symbols_text_input(driver, payload):
    page_input = PageInput(driver, 'simple')
    page_input.open_page()
    page_input.find_element(By.ID, 'id_text_string')
    page_input.entered_end_submit_field(payload)
    page_input.find_element(By.ID, 'error_1_id_text_string')
    page_input.check_result(
        'Please enter no more than 25 characters'
    )
#
# # def test_empty_text_input(driver):
# #     page_input = PageInput(driver, 'simple')
# #     page_input.open_page()
# #     page_input.find_element(By.ID, 'id_text_string')
# #     page_input.entered_end_submit_field('')
# #     page_input.browser_validate(
# #         'return arguments[0].checkValidity();'
# #     )
# #     # page_input.check_result()
#

'''TestEmailInput'''
@pytest.mark.parametrize('payload', validDataEmail)
def test_valid_email_input(driver, payload):
    page_input = PageInput(driver, 'email')
    page_input.open_page()
    page_input.find_element(By.ID, 'id_email')
    page_input.entered_end_submit_field(payload)
    page_input.find_element(By.ID, 'result-text')
    page_input.check_result(payload)


@pytest.mark.parametrize('payload', invalidDataEmail)
def test_invalid_email_input(driver, payload):
    page_input = PageInput(driver, 'email')
    page_input.open_page()
    page_input.find_element(By.ID, 'id_email')
    page_input.entered_end_submit_field(payload)
    page_input.find_element(By.ID, 'error_1_id_email')
    page_input.check_result(
        'Enter a valid email address.'
    )

'''TestPasswordInput'''
@pytest.mark.parametrize('payload', validDataPassword)
def test_valid_password_input(driver, payload):
    page_input = PageInput(driver, 'passwd')
    page_input.open_page()
    page_input.find_element(By.ID, 'id_password')
    page_input.entered_end_submit_field(payload)
    page_input.find_element(By.ID, 'result-text')
    page_input.check_result(payload)


@pytest.mark.parametrize('payload', invalidDataPassword)
def test_invalid_password_input(driver, payload):
    page_input = PageInput(driver, 'passwd')
    page_input.open_page()
    page_input.find_element(By.ID, 'id_password')
    page_input.entered_end_submit_field(payload)
    page_input.find_element(By.ID, 'error_1_id_password')
    page_input.check_result(
        'Low password complexity'
    )

