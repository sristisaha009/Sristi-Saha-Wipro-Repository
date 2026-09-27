from selenium import webdriver
from login_page import LoginPage
from dashboard_page import DashboardPage
import time

driver = webdriver.Chrome()
try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert dashboard_page.is_dashboard_displayed(), \
        "Dashboard was not displayed after valid login."

    assert dashboard_page.get_page_title() == "Products", \
        "Products title was not displayed."

    print("TEST 1 PASSED: Valid login successful.")

finally:
    time.sleep(5)
    driver.quit()