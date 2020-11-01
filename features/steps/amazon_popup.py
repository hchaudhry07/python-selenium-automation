# 0.) Repeat everything I coded during the class.

from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_POPUP = (By.CSS_SELECTOR, "#nav-signin-tooltip > a")

@given("Open Amazon")
def open_page(context):
    context.driver.get("https://www.amazon.com/")

@then("Sign-In Popup is present and clickable")
def sign_in(context):
    context.driver.wait.until(EC.presence_of_element_located(SIGN_IN_POPUP))
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP))

@when("Sign-In Popup disappears")
def dis_appears(context):
    context.driver.wait.until(EC.invisibility_of_element(SIGN_IN_POPUP))

@then("Verify Sign-In Popup is not clickable")
def no_click_popup(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_POPUP))