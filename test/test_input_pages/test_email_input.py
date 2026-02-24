import pytest
from data.test_data_imputs import validPayloadEmail as validDataEmail
from data.test_data_imputs import invalidPayloadEmail as invalidDataEmail


def test_check_h1_text(email_input_page):
    email_input_page.open_page()
    email_input_page.check_h1_text()

@pytest.mark.parametrize('payload', validDataEmail)
def test_valid_email_input(email_input_page, payload):
    email_input_page.open_page()
    email_input_page.send_keys_to_email_input(payload)
    email_input_page.submit_email_input()
    email_input_page.check_valid_result_email_input(payload)

@pytest.mark.parametrize('payload', invalidDataEmail)
def test_invalid_email_input(email_input_page, payload):
    email_input_page.open_page()
    email_input_page.send_keys_to_email_input(payload)
    email_input_page.submit_email_input()
    email_input_page.check_invalid_result_email_input()




