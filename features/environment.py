from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='/Users/hasnainchaudhry/AUTOMATION/python-selenium-automation/chromedriver')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

# H.W. #7 - Part #0.) - - Repeat everything I coded during the class.
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)
# This is the end of H.W. #7 - Part #0.). Thank you!

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()



