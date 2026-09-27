from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    print("JavaScript Alerts page opened.")

    # Javascript alert
    alert_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Click for JS Alert']")
        )
    )

    alert_button.click()
    alert = wait.until(EC.alert_is_present())
    print("Alert message:", alert.text)
    alert.accept()
    print("Alert accepted.")

    #javascript confirm
    confirm_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Click for JS Confirm']")
        )
    )

    confirm_button.click()
    confirm = wait.until(EC.alert_is_present())
    print("Confirm message:", confirm.text)
    confirm.dismiss()
    print("Confirm dismissed.")

    # Javascript prompt
    prompt_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Click for JS Prompt']")
        )
    )

    prompt_button.click()
    prompt = wait.until(EC.alert_is_present())
    print("Prompt message:", prompt.text)
    prompt.send_keys("Selenium Test")
    print("Text entered into prompt.")
    prompt.accept()
    print("Prompt accepted.")
    print("Assignment 4 PASSED")

finally:
    driver.quit()