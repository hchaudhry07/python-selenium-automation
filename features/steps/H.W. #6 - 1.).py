# 1. Create a window handling test case from the class and verify that user can open amazon applications from Terms of Conditions
# https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088

from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

WEB_LINK = (By.XPATH, "//a[text()='Amazon applications']")
WEB_PAGE = (By.CSS_SELECTOR, "a.help-display-cond")

@given("Open Amazon T&C page")
def Open_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")

@then("Store original windows")
def window_store(context):
    context.original_window = context.driver.current_window_handle

@then("Click on Amazon applications link")
def click_amazon_app(context):
    link = context.driver.wait.until(EC.element_to_be_clickable(WEB_LINK))
    link.click()

@then("Switch to the newly opened window")
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.original_windows = context.driver.window_handles
    context.driver.switch_to.window(context.original_windows[1])

@then("Amazon app page is opened")
def app_page_open(context):
    assert context.driver.title == "Amazon Mobile Shopping Apps", f"Error! Expected 'Amazon applications page!' but got {context.original_windows[0]}"

@then("User can close new window and switch back to original")
def switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_windows[0])
    assert context.driver.title == "Amazon.com Help: Conditions of Use", f'Error! Expected "Amazon.com Help" but got {context.driver.title}'
