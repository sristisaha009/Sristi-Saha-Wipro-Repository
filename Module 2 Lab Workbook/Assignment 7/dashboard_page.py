from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCTS_TITLE)
        ).text

    def is_dashboard_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.PRODUCTS_TITLE)
            ).is_displayed()
        except:
            return False