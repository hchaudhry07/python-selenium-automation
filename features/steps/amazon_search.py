from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT =(By.ID, 'twotabsearchtextbox')
SEARCH_ICON =(By.XPATH, "//input[@value = 'Go']")
SEARCH_RESULT =(By.XPATH, "//span[@class='a-color-state a-text-bold']")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input Guitar into Amazon search field')
def input_search_word(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys('Guitar')

@when('Click on Amazon search icon')
def click_search_icon(context):
    search_icon = context.driver.find_element(*SEARCH_ICON)
    search_icon.click()

@then('Search results for Guitar are shown')
def verify_search_result(context):
    search_result = context.driver.find_element(*SEARCH_RESULT)
    assert search_result.text == '"Guitar"', f'Error. Expected Guitar, but got {search_result.text}'


