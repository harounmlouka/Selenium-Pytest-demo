from pages.wikipedia_home_page import WikipediaHomePage
from pages.wikipedia_results_page import WikipediaResultsPage

from utils.data_loader import load_test_data


def test_wikipedia_search(driver):

    data = load_test_data("data/search_data.json")

    home_page = WikipediaHomePage(driver)
    results_page = WikipediaResultsPage(driver)

    home_page.open()

    home_page.search(data["search_term"])

    assert results_page.title_contains("Selenium")