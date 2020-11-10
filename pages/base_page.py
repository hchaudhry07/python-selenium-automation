# H.W. #7 - Part #0.) - - Repeat everything I coded during the class.
from selenium.webdriver.support.wait import WebDriverWait

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text: str, *locator):
        """
        Search for a webelement, get its text, compare with expected_text
        :param expected_text: Text to be in webelement
        :param locator: Search strategy and locator of webelement (ex. (By.ID, 'id'))
        """
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} does not match {actual_text}"

# H.W. #7 - - Part #2*.) Write this scenarios to use Page Object pattern:

    def verify_items_listed(self, expected_text: str, *locator):
        item_list = self.driver.find_element(*locator)
        for i in range(len(str(item_list))):
            assert expected_text == {item_list.text},\
                f"The list of Items don't match. Expected {item_list}, however, we got {expected_text}"

    def verify_items_counted(self, expected_count, *locator):
        item_boxes = len(self.driver.find_element(*locator))
        assert int(expected_count), f"Error. Expected {expected_count} but got {item_boxes}"


