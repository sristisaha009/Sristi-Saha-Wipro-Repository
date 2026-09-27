from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )
    INVENTORY_CONTAINER = (
        By.ID,
        "inventory_container"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.USERNAME
            )
        )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        )
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        ).click()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        ).text

    def is_inventory_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.INVENTORY_CONTAINER
            )
        ).is_displayed()