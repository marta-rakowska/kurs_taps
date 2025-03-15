from helpers.support_functions import *

my_account_header = '//*[@id="post-9"]/header/h1'
my_account_tab = '//*[@id="post-9"]/div/div/nav/ul/li[1]/a'
orders_tab = '//*[@id="post-9"]/div/div/nav/ul/li[2]/a'
downloads_tab = '//*[@id="post-9"]/div/div/nav/ul/li[3]/a'
address_tab = '//*[@id="post-9"]/div/div/nav/ul/li[4]/a'
edit_account_tab = '//*[@id="post-9"]/div/div/nav/ul/li[5]/a'
logout_button = '//*[@id="post-9"]/div/div/nav/ul/li[6]/a'


def my_account_header_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, my_account_header)
    return elem.is_displayed()


def go_to_my_account_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_tab)
    elem = driver_instance.find_element(By.XPATH, my_account_tab)
    elem.click()


def go_to_orders_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, orders_tab)
    elem = driver_instance.find_element(By.XPATH, orders_tab)
    elem.click()


def orders_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_header)
    elem = driver_instance.find_element(By.XPATH, my_account_header)
    header_text = 'Zamówienia'
    if elem.text == header_text:
        return True
    else:
        return False


def go_to_downloads_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, downloads_tab)
    elem = driver_instance.find_element(By.XPATH, downloads_tab)
    elem.click()


def downloads_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_header)
    elem = driver_instance.find_element(By.XPATH, my_account_header)
    header_text = 'Pliki do pobrania'
    if elem.text == header_text:
        return True
    else:
        return False


def go_to_address_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, address_tab)
    elem = driver_instance.find_element(By.XPATH, address_tab)
    elem.click()


def address_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_header)
    elem = driver_instance.find_element(By.XPATH, my_account_header)
    header_text = 'Adresy'
    if elem.text == header_text:
        return True
    else:
        return False


def go_to_edit_account_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, edit_account_tab)
    elem = driver_instance.find_element(By.XPATH, edit_account_tab)
    elem.click()


def edit_account_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_header)
    elem = driver_instance.find_element(By.XPATH, my_account_header)
    header_text = 'Szczegóły konta'
    if elem.text == header_text:
        return True
    else:
        return False


def logout_from_your_account(driver_instance):
    wait_for_visibility_of_element(driver_instance, logout_button)
    elem = driver_instance.find_element(By.XPATH, logout_button)
    elem.click()

