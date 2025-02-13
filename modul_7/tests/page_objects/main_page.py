from helpers.support_functions import *

main_page_header = '//*[@id="test-header"]'
main_page_content = '//*[@id="test-content"]'


def content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, main_page_content)
    return elem.is_displayed()
