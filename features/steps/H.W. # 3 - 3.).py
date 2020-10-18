# 3.) Create a test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Shopping Cart is empty.

from behave import given, when, then
from selenium.webdriver.common.by import By


@given("Open Amazon website")
def opa_web(context):
    context.driver.get("https://www.amazon.com/")

@when("Clicking on 'Cart'")
def click_cart(context):
    context.driver.find_element(By.ID, "nav-cart").click()

@then("Verify if Amazon displays your cart as empty")
def verify_amazon(context):
    amazon_verify = context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Your Amazon')]")
    assert "Your Amazon Cart is empty" in amazon_verify.text, f"Expected, 'Your Amazon Cart is empty' but got {amazon_verify.text}"

