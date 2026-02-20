import pytest
from endpoint.endpoints import MobileTest

@pytest.mark.Text_url
def test_input_field(mobile_driver):
    page = MobileTest(mobile_driver, 'https://www.qa-practice.com/elements/input/simple')
    page.driver.get(page.base_url)
    page.select_text_field()
    page.check_text_field()




