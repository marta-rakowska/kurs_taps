from helpers.support_functions import *

hovers_tab = '//*[@id="hovers-header"]'
hovers_content = '//*[@id="hovers-content"]'
gentlemans_pic = '//*[@id="hovers-content"]/div/div[1]/img'
gentleman_link = '//*[@id="hovers-content"]/div/div[1]/div/a'


def click_hovers_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, hovers_tab)
    elem = driver_instance.find_element(By.XPATH, hovers_tab)
    elem.click()


def hover_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, hovers_content)
    return elem.is_displayed()


def hover_over_element_and_click(driver_instance):
    hover_over_element(driver_instance, gentlemans_pic)
    elem = driver_instance.find_element(By.XPATH, gentleman_link)
    elem.click()
