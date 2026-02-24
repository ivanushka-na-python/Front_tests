import pytest
from data.test_data_imputs import validPayloadPassword as validDataPassword
from data.test_data_imputs import invalidPayloadPassword as invalidDataPassword

def test_check_h1_text(password_input_page):
    password_input_page.open()
    password_input_page.check_h1_text()



@pytest.mark.parametrize('payload', validDataPassword)
def test_valid_passwd_input(password_input_page, payload):
    password_input_page.open_page()
    password_input_page.send_keys_to_passwd_input(payload)
    password_input_page.submit_passwd_input()
    password_input_page.check_valid_result_passwd_input(payload)

@pytest.mark.parametrize('payload', invalidDataPassword)
def test_valid_passwd_input(password_input_page, payload):
    password_input_page.open_page()
    password_input_page.send_keys_to_passwd_input(payload)
    password_input_page.submit_passwd_input()
    password_input_page.check_invalid_result_passwd_input()
