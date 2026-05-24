from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WikipediaHomePage(BasePage):

    URL = "https://www.wikipedia.org/"

    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.driver.get(self.URL)

    def search(self, text):
        self.type(self.SEARCH_INPUT, text)
        self.click(self.SEARCH_BUTTON)