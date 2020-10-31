# 1. Make a test case similar to the example from class, use https://www.amazon.com/gp/product/B07BJKRR25/ color selection OR ANY OTHER ITEM.
# Create 1 test case that will loop through colors (in any way you prefer)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name span.selection')


@given("Go Open Amazon Men's Pants {productid} Page")
def Open_page(context, productid):
    context.driver.get("https://www.amazon.com/gp/product/B07BJKRR25/")

@then("Verify Users can select different colors")
def pant_color_verify(context):
    expected_colors = ['Black', 'Dark Vintage', 'Dark Wash', 'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage', 'Washed Black', 'Indigo Wash', 'Vintage Light Wash', 'Blue Overdyed']
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        color_text = context.driver.find_element(*SELECTED_COLOR).text
        assert color_text == expected_colors[i], \
            f"Color don't match. Expected {expected_colors[i]} but got {color_text}"
