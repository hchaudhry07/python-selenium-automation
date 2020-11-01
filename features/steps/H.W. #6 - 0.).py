# 0.) Repeat everything I coded during the class.

from behave import given, then
from selenium.webdriver.common.by import By

ITEMS = (By.CSS_SELECTOR, "#wfm-pmd_deals_section div:nth-of-type(6) li")
PRODUCT_NAME = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")
@given("Open WholeFoods")
def open_amazon_product(context):
    context.driver.get("https://www.amazon.com/wholefoodsdeals")

@then("Each Item has Regular field and Product name")
def verify_each_item(context):
    all_items = context.driver.find_elements(*ITEMS)
    for item in all_items:
        assert "Regular" in item.text, f"Expected 'Regular' to be in {item.text}"
        assert item.find_element(*PRODUCT_NAME)