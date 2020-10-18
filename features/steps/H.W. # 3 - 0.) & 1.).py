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


# 2.) Update a test case for support search using BDD
# User can search for Cancelling an order on Amazon (test case from Ex 2 of HW2)

@given("Open Amazon help page")
def help_pg(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")

@when("Searching for 'Cancelling Orders'")
def click_bait(context):
    click_btn = context.driver.find_element(By.ID, 'helpsearch')
    click_btn.click()
    click_btn.send_keys("Cancelling Orders")
    click_btn.send_keys(Keys.ENTER)

@Then("Verify if user can see option to Cancelling Orders")
def verify_it(context):
    v_search = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Cancel Items or Orders')]")
    assert "Cancel Items or Orders" in v_search.text, f"Expected 'Cancel Items or Orders', but got {v_search.text}"





