from pages.base_page import BasePage


class WikipediaResultsPage(BasePage):

    def title_contains(self, text):
        return text in self.get_title()