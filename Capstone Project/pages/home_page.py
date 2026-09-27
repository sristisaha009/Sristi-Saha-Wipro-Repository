from selenium.webdriver.common.by import By
from framework.base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")

    def open(self, base_url):
        self.driver.get(base_url)
        self.wait.until(lambda d: d.title != "")
        return self

    def search_for(self, keyword):
        self.type_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)
        return SearchResultsPage(self.driver)

from pages.search_results_page import SearchResultsPage
