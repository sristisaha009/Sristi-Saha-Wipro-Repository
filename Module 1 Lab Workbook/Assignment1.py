from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(
        By.XPATH, "//input[@type='submit']"
    )
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )
    current_url = driver.current_url

    assert "/inventory.html" in current_url
    print("Assignment 1 PASSED")
    print("Login successful!")
    print("Current URL:", current_url)

finally:
    driver.quit()