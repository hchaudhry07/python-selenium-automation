from behave import given, then
from selenium.webdriver.common.by import By

BENEFIT_BOXES = (By.CSS_SELECTOR, "div.benefit-box")

@given("Open Amazon Prime page")
def open_amazon_prime(context):
    context.driver.get("https://www.amazon.com/amazonprime?_encoding=UTF8&ref_=nav_prime_try_btn")

@then("Verify {expected_count} benefit boxes are displayed")
def verify_box_count(context, expected_count):
    boxes = len(context.driver.find_elements(*BENEFIT_BOXES))
    assert boxes == int(expected_count), f'Amount of boxes incorrect. Expected 8, but got {boxes}'


