from helpers.support_functions import *

iframe_tab = 'iframe-header'
iframe_main = 'iframe'
button1 = 'simpleButton1'
message = 'whichButtonIsClickedMessage'


def click_iframe_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, iframe_tab)
    elem.click()


def click_button1(driver_instance):
    wait_for_visibility_of_element(driver_instance, iframe_main, time_to_wait=5)
    driver_instance.switch_to.frame(driver_instance.find_element(By.TAG_NAME, 'iframe'))
    driver_instance.find_element(By.ID, button1).click()
    output = driver_instance.find_element(By.ID, message).text
    if output == 'Button 1 was clicked!':
        return True
    else:
        return False
