from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import  when, then
from app.application import Application
AMAZON_MUSIC_ITEMS = (By.CSS_SELECTOR, "ul.hmenu-translateX a")

# H.W. #7 - - Part #1.) Rewrite these scenarios to use Page Object pattern:
@when("Click Amazon Orders link")
def click_amazon_orders(context):
    context.app.main_page.click_sign_in()

@then("Verify Sign In page is opened")
def verify_sign_in_page(context):
    context.app.search_results_page.verify_sign_in_page('Sign-In')

@when("Click on cart icon")
def click_cart(context):
    context.app.main_page.click_cart()

@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_cart_page(context):
    context.app.search_results_page.verify_cart_page('Your Amazon Cart is empty')

# H.W. #7 - - Part #2*.) Write this scenarios to use Page Object pattern:

@when("Click on hamburger menu")
def click_hamburger(context):
    context.app.main_page.click_hamburger()

@when("Click on Amazon Music menu item")
def amazon_music(context):
    context.app.main_page.amazon_music()

@then("7 menu items are present")
def verify_amazon_music_menu_items(context):
    links = context.driver.find_element(*AMAZON_MUSIC_ITEMS).text
    context.app.search_results_page.verify_amazon_music_menu_items(links)
    context.app.search_results_page.verify_music_menu_item_count()


