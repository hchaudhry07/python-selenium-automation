# 1. [If you did not do that in HW3!] Create your own test case to add any product you want into the cart,
# and make sure it’s there (check for the number of items in the cart OR open the cart
# and verify it’s there, up to you!)

from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

FIT_SECTION = (By.CSS_SELECTOR, "div.a-spacing-none img.landscape-image")
COOL_OUTFIT = (By.XPATH, "//img[@alt = 'Kooy Inflatable Alien Costume for Adult (Adult - Et Alien)']")
FIT_CART = (By.ID, "add-to-cart-button")
SEARCH_CAM = (By.CSS_SELECTOR, "input.nav-input")
FLY_CAM = (By.XPATH, "//div[@data-cel-widget='search_result_2']")
SHOP_CART = (By.ID, "nav-cart")
CART_VERIFY = (By.CSS_SELECTOR, "form#activeCartViewForm")

@given("Open up the Amazon page")
def amazon_page(context):
    context.driver.get("https://www.amazon.com/")

@when("Search for Costume for Men")
def dress_up(context):
    dress_down = context.driver.find_element(*SEARCH_CAM)
    dress_down.click()
    dress_down.send_keys("Costume for Men")
    dress_down.send_keys(Keys.ENTER)

@then("Click on the awesome costume there")
def pick_outfit(context):
    cost_ume = context.driver.find_element(*COOL_OUTFIT)
    cost_ume.click()

@then("Add the Costume to cart")
def add_to_cart(context):
    cart_add = context.driver.find_element(*FIT_CART)
    cart_add.click()

@when("Input drones into search bar")
def search_bar(context):
    input_search = context.driver.find_element(*SEARCH_CAM)
    input_search.click()
    input_search.send_keys("Drones")
    input_search.send_keys(Keys.ENTER)

@then("Click on the Drone you like")
def select_drone(context):
    fly_drone = context.driver.find_element(*FLY_CAM)
    fly_drone.click()

@then("Add the Drone to cart")
def add_drone(context):
    drone_add = context.driver.find_element(*FIT_CART)
    drone_add.click()


@then("Click on Shopping Cart icon")
def shop_cart(context):
    cart_shop = context.driver.find_element(*SHOP_CART)
    cart_shop.click()

@then("Verify the items are there")
def verify_items(context):
    item_verify_cart = context.driver.find_element(*CART_VERIFY)
    if item_verify_cart.text != "Costume" and "Drone":
        print("Items are indeed in the cart!")
    else:
        print("The Items are not in the cart!")

