from helpers.support_functions import *

add_to_cart_button = '//*[@id="product-46"]/div[2]/form/button'
added_to_cart_alert = '//*[@id="content"]/div/div[1]/div'
quantity_input = '//*[@id="quantity_67d57db04ff54"]'
description_tab = '//*[@id="tab-title-description"]/a'
description_tab_header = '//*[@id="tab-description"]/h2'
additional_information_tab = '//*[@id="tab-title-additional_information"]/a'
additional_information_tab_header = '//*[@id="tab-additional_information"]/h2'
reviews_tab = '//*[@id="tab-title-reviews"]/a'
reviews_tab_header = '//*[@id="comments"]/h2'
fifth_star = '//*[@id="commentform"]/div/p/span/a[5]'
review_input = '//*[@id="comment"]'
author_name_input = '//*[@id="author"]'
author_email_input = '//*[@id="email"]'
submit_button = '//*[@id="submit"]'
add_review_error_message = '//*[@id="error-page"]/div'

review_text = "Good quality. Beautiful color."
author_name = 'Cotaga'
author_email = 'cotaga1249@maillei.net'
add_review_error_message_text = 'proszę wypełnić wymagane pola'


def change_quantity_to_2(driver_instance):
    elem = driver_instance.find_element(By.XPATH, quantity_input)
    elem.clear()
    elem.send_keys(2)


def add_to_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, add_to_cart_button)
    elem.click()


def added_to_cart_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, added_to_cart_alert)
    elem = driver_instance.find_element(By.XPATH, added_to_cart_alert)
    elem.is_displayed()


def go_to_description_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, description_tab)
    elem.click()


def description_tab_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, description_tab_header)
    elem = driver_instance.find_element(By.XPATH, description_tab_header)
    elem.is_displayed()


def go_to_additional_information_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, additional_information_tab)
    elem.click()


def additional_information_tab_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, additional_information_tab_header)
    elem = driver_instance.find_element(By.XPATH, additional_information_tab_header)
    elem.is_displayed()


def go_to_reviews_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, reviews_tab)
    elem.click()


def reviews_tab_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, reviews_tab_header)
    elem = driver_instance.find_element(By.XPATH, reviews_tab_header)
    elem.is_displayed()


def add_five_stars_rating(driver_instance):
    elem = driver_instance.find_element(By.XPATH, fifth_star)
    elem.click()


def add_review_text(driver_instance):
    elem = driver_instance.find_element(By.XPATH, review_input)
    elem.send_keys(review_text)


def add_author_name(driver_instance):
    elem = driver_instance.find_element(By.XPATH, author_name_input)
    elem.send_keys(author_name)


def add_author_email(driver_instance):
    elem = driver_instance.find_element(By.XPATH, author_email_input)
    elem.send_keys(author_email)


def submit_review(driver_instance):
    elem = driver_instance.find_element(By.XPATH, submit_button)
    elem.click()


def add_valid_review(driver_instance):
    add_five_stars_rating(driver_instance)
    add_review_text(driver_instance)
    add_author_name(driver_instance)
    add_author_email(driver_instance)
    submit_review(driver_instance)


def add_empty_review(driver_instance):
    submit_review(driver_instance)


def add_review_without_rating(driver_instance):
    add_review_text(driver_instance)
    add_author_name(driver_instance)
    add_author_email(driver_instance)
    submit_review(driver_instance)


def add_review_without_text(driver_instance):
    add_five_stars_rating(driver_instance)
    add_author_name(driver_instance)
    add_author_email(driver_instance)
    submit_review(driver_instance)


def add_review_without_author_name(driver_instance):
    add_five_stars_rating(driver_instance)
    add_review_text(driver_instance)
    add_author_email(driver_instance)
    submit_review(driver_instance)


def add_review_without_author_email(driver_instance):
    add_five_stars_rating(driver_instance)
    add_review_text(driver_instance)
    add_author_name(driver_instance)
    submit_review(driver_instance)


def add_review_error_message_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, add_review_error_message)
    elem = driver_instance.find_element(By.XPATH, add_review_error_message)
    if add_review_error_message_text in elem.text:
        return True
    else:
        return False








