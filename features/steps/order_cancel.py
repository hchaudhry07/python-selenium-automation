from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Strategy for locators on the following features:
# Continue button, search by id 'continue'
# Need help link, search by class 'a-expander-prompt'
# Forgot your password link, search by class 'a-link-normal'

# driver.get('https://www.amazon.com/')

# Init driver
driver = webdriver.Chrome(executable_path='/Users/hasnainchaudhry/AUTOMATION/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)

# Open to Amazon help page
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# Locate Find More Solutions search bar
more_solutions = driver.find_element(By.ID, 'helpsearch')
more_solutions.click()

# Input 'Cancel Order'
cancel_order = driver.find_element(By.ID, 'helpsearch')
cancel_order.send_keys('Cancel Order')

# Click 'Go'
srch_now = driver.find_element(By.ID, 'helpsearch')
srch_now.send_keys(Keys.ENTER)

# Verify if 'Cancel Items or Orders' is shown
srch_result = driver.find_element(By.XPATH, "//h1[contains(text(), 'Cancel Items')]").text

if srch_result == "Cancel Items or Orders":
    print("Test case has passed")
else:
    print("Test case has failed")

driver.quit()


