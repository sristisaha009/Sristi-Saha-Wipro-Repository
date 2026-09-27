from selenium.webdriver.common.by import By
from framework.base_page import BasePage

class SearchResultsPage(BasePage):
    HEADING = (By.CSS_SELECTOR, "#content h1")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "div.product-thumb")
    EMPTY_MESSAGE = (By.XPATH, "//*[contains(normalize-space(), 'There is no product that matches')]")

    def heading(self):
        return self.get_text(self.HEADING)

    def product_count(self):
        self.wait.until(lambda d: d.find_elements(*self.PRODUCT_CARDS) or
                        d.find_elements(*self.EMPTY_MESSAGE))
        return len(self.driver.find_elements(*self.PRODUCT_CARDS))

    def product_names(self):
        cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        names = []
        for card in cards:
            title = card.find_elements(By.CSS_SELECTOR, ".caption h4 a")
            if title:
                names.append(title[0].text.strip())
        return names
