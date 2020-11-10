# H.W. #7 - Part #0.) - - Repeat everything I coded during the class.
from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.XPATH, "//input[@value = 'Go']")
    SIGN_IN = (By.CSS_SELECTOR, "a#nav-link-accountList")
    CLICK_CART = (By.CSS_SELECTOR, "a#nav-cart")
    HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')
    CLICK_AMAZON_MUSIC = (By.XPATH, "//div[contains(text(), 'Amazon Music')]")

    def open_amazon(self):
        self.open_page('https://www.amazon.com/')

    def input_search_word(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)

    def click_search_icon(self):
        self.click(*self.SEARCH_ICON)

# H.W. #7 - - Part #1.) Rewrite these scenarios to use Page Object pattern:
    def click_sign_in(self):
        self.click(*self.SIGN_IN)

    def click_cart(self):
        self.click(*self.CLICK_CART)

# H.W. #7 - - Part #2*.) Write this scenarios to use Page Object pattern:
    def click_hamburger(self):
        self.click(*self.HAM_MENU_ICON)

    def amazon_music(self):
        self.click(*self.CLICK_AMAZON_MUSIC)


