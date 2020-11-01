# 0.) Repeat everything I coded during the class.

from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

WEB_LINK = (By.XPATH, "//a[contains(text(), 'spicyfattyburger')]")
WEB_NAME = (By.XPATH, "//*[contains(text(), 'Spicy Fatty')]")

@given("Open Yelp Page")
def yelp_page(context):
    context.driver.get("https://www.yelp.com/biz/spicy-fatty-burger-queens")

@when("Click on Website Link")
def web_link(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle
    link = context.driver.find_element(*WEB_LINK)
    link.click()
    print(context.original_windows)
    print(context.original_window)

@when("Switch to a new window")
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.new_windows = context.driver.window_handles
    print(context.new_windows)
    for window in context.original_windows:
        context.new_windows.remove(window)
    print(context.new_windows)
    context.driver.switch_to_window(context.new_windows[0])

@then("The Table Website is open")
def table_website(context):
    context.driver.find_element(*WEB_NAME)

@then("A user can close the new window and go to the original")
def window_close(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)