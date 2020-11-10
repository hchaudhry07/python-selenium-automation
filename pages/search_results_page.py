# H.W. #7 - Part #0.) - - Repeat everything I coded during the class.
from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SIGN_IN_PAGE = (By.XPATH, "h1.a-spacing-small")
    SHOPPING_CART_PAGE = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty")
    AMAZON_MUSIC_ITEMS = (By.CSS_SELECTOR, "ul.hmenu-translateX a")

    def verify_search_result(self, expected_text: str):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

# H.W. #7 - - Part #1.) Rewrite these scenarios to use Page Object pattern:
    def verify_sign_in_page(self, expected_text: str):
        self.verify_text(expected_text, *self.SIGN_IN_PAGE)

    def verify_cart_page(self, expected_text: str):
        self.verify_text(expected_text, *self.SHOPPING_CART_PAGE)

# H.W. #7 - - Part #2*.) Write this scenarios to use Page Object pattern:
    def verify_amazon_music_menu_items(self, expected_text: str):
        self.verify_items_listed(expected_text, *self.AMAZON_MUSIC_ITEMS)

    def verify_music_menu_item_count(self, expected_count: int):
        self.verify_items_counted(expected_count, *self.AMAZON_MUSIC_ITEMS)
