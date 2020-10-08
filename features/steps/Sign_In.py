from selenium.webdriver.common.by import By
from behave import given, when, then


@given ('Open New Amazon Page')
def open_new(context):
    context.driver.get('https://www.amazon.com')

@when('Click on Orders')
def click_order(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify if sign in is prompted')
def verify_sign_in(context):
    verify = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign-In')]").text
    if verify == "Sign In":
        print("Test Passed")
    else:
        print("Test Failed")

    context.driver.quit()



