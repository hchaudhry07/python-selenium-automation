# 2.) Create a test case that will open amazon BestSellers page: https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers
# And verify there are 5 links:

from behave import given, when, then
from selenium.webdriver.common.by import By

BEST_LINKS = (By.ID, "zg_tabs")

@given("Open Amazon BestSeller Page")
def best_seller(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")

@then("Verify if {expected_count} links are present")
def verify_links(context, expected_count):
    links = len(context.driver.find_elements(*BEST_LINKS))
    assert int(expected_count) != links, f'Amount of links incorrect. Expected {expected_count}, but got {links}'
    very_fied = context.driver.find_element(*BEST_LINKS)
    print(very_fied.text)
