# 0.) Repeating the code you did in the lesson.

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SEARCH_BAR =(By.CSS_SELECTOR, "input.nav-input[type=text]")
VERIFY_SRCH =(By.CSS_SELECTOR, "span.a-color-state")

@given("Open the Amazon page")
def open_page(context):
    context.driver.get("https://www.amazon.com")

@when('Input "Glasses" and click search')
def input_search(context):
    input_key = context.driver.find_element(*SEARCH_BAR)
    input_key.click()
    input_key.send_keys('Glasses')
    input_key.send_keys(Keys.ENTER)

@then('Verify that page contains "Glasses"')
def verify_result(context):
    v_result = context.driver.find_element(*VERIFY_SRCH)
    assert "Glasses" in v_result.text, f"Expected 'Glasses', but got {v_result.text}"


# 1.) Finding the most optimal locators for Create Account (Registration) page elements:
# Amazon Logo => (By.CSS_SELECTOR, "i.a-icon-logo")
# Create Account Logo => (By.CSS_SELECTOR, "h1.a-spacing-small")
# 'Your Name' Field => (By.ID, "ap_customer_name")
# 'Email' Field => (By.XPATH, "//input[@type='email']")
# 'Password' Field => (By.XPATH, "//input[@id='ap_password']")
# 'Re-Enter Password' Field => (By.XPATH, "//input[@id='ap_password_check']")
# 'Create your Amazon account' Field => (By.ID, "continue")
# 'Conditions of Use' Link => (By.XPATH, "//*[contains(@href, 'condition')]")
# 'Privacy Notice' Link => (By.XPATH, "//a[contains(@href, 'register_notification_privacy')]")
# 'Sign In' link => (By.CSS_SELECTOR, "a.a-link-emphasis")

#



