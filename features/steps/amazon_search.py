from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from app.application import Application

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.XPATH, "//input[@value = 'Go']")
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip >a")

# H.W. #7 - Part #0.) - - Repeat everything I coded during the class.
@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_amazon()

@when('Input Guitar into Amazon search field')
def input_search_word(context):
    context.app.main_page.input_search_word('Guitar')

@when('Click on Amazon search icon')
def click_search_icon(context):
    context.app.main_page.click_search_icon()

@then('Search results for Guitar are shown')
def verify_search_result(context):
    context.app.search_results_page.verify_search_result('"Guitar"')
# This is the end of H.W. #7 - Part #0.). Thank you!

# HW5
# 0. Repeat everything I coded during the class.

@then("Verify Sign In is clickable")
def verify_sign_in_click(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN))


@then("Verify Sign In disappears")
def verify_sign_in_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_BTN))

