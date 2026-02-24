from data.test_data_imputs import validPayloadSimple as validData
from data.test_data_imputs import invalidPayloadSimple as invalidData
from data.test_data_imputs import invalid1PayloadSimple as invalidData1
from data.test_data_imputs import invalid25PayloadSimple as invalidData25


import pytest


def test_check_h1_text(simple_input_page):
    simple_input_page.open_page()
    simple_input_page.check_h1_text()


@pytest.mark.parametrize('payload', validData)
def test_valid_text_input(simple_input_page, payload):
    simple_input_page.open_page()
    simple_input_page.send_keys_to_text_input(payload)
    simple_input_page.submit_text_input()
    simple_input_page.check_valid_result_text_input(payload)


@pytest.mark.parametrize('payload', invalidData)
def test_invalid_text_input(simple_input_page, payload):
    simple_input_page.open_page()
    simple_input_page.send_keys_to_text_input(payload)
    simple_input_page.submit_text_input()
    simple_input_page.check_invalid_result_text_input()


@pytest.mark.parametrize('payload', invalidData1)
def test_invalid_1_input_text(simple_input_page, payload):
    simple_input_page.open_page()
    simple_input_page.send_keys_to_text_input(payload)
    simple_input_page.submit_text_input()
    simple_input_page.check_invalid_1_result_text_input()


@pytest.mark.parametrize('payload', invalidData25)
def test_invalid_25_input_text(simple_input_page, payload):
    simple_input_page.open_page()
    simple_input_page.send_keys_to_text_input(payload)
    simple_input_page.submit_text_input()
    simple_input_page.check_invalid_25_result_text_input()



