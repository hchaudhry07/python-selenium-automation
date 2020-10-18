# 2.) Update a test case for support search using BDD
# User can search for Cancelling an order on Amazon (test case from Ex 2 of HW2)

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given("Open Amazon help page")
def help_pg(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")

@when("Searching for 'Cancelling Orders'")
def click_bait(context):
    click_btn = context.driver.find_element(By.ID, 'helpsearch')
    click_btn.click()
    click_btn.send_keys("Cancelling Orders")
    click_btn.send_keys(Keys.ENTER)

@then("Verify if user can see option to Cancelling Orders")
def verify_it(context):
    v_search = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Cancel Items or Orders')]")
    assert "Cancel Items or Orders" in v_search.text, f"Expected 'Cancel Items or Orders', but got {v_search.text}"
