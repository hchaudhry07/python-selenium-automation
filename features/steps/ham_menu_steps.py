from behave import when, then
from selenium.webdriver.common.by import By

HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')
VISIBLE_LINKS = (By.CSS_SELECTOR, "ul.hmenu-visible a.hmenu-item")

@when("Click to Open Amazon Hamburger Menu")
def click_ham_menu(context):
    context.driver.find_element(*HAM_MENU_ICON).click()

@then("Verify {expected_count} links are visible")
def verify_links_count(context, expected_count):
    links = len(context.driver.find_elements(*VISIBLE_LINKS))
    assert int(expected_count) != links, f'Amount of links incorrect. Expected {expected_count}, but got {links}'