from selenium.webdriver.common.by import By
from framework.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    WARNING = (By.CSS_SELECTOR, ".alert.alert-danger")

    def open(self, base_url):
        self.driver.get(base_url.rstrip("/") + "/index.php?route=account/login")
        self.wait.until(lambda d: "login" in d.current_url.lower())
        return self

    def login(self, email, password):
        self.type_text(self.EMAIL, email)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def warning_text(self):
        return self.get_text(self.WARNING)
