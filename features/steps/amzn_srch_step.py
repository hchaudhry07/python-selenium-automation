from selenium.webdriver.common.by import By
from behave import then

SEARCH_INPUT =(By.ID, 'twotabsearchtextbox')

@then('Verify input value is Guitar')
def verify_input_value(context):
    Input_value = context.driver.find_element(*SEARCH_INPUT)
    Input_value.text == context.driver.find_element(*SEARCH_INPUT)

