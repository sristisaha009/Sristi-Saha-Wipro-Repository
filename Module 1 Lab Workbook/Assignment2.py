from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get(
        "https://the-internet.herokuapp.com/dynamic_loading/1"
    )
    driver.maximize_window()
    print("Page opened successfully.")

    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Start']")
        )
    )
    print("Start button found.")

    start_button.click()

    print("Waiting for dynamic content...")

    text_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='finish']/h4")
        )
    )

    text = text_element.text
    print("Dynamic content:", text)
    assert text == "Hello World!"
    print("Assignment 2 PASSED")

finally:
    driver.quit()