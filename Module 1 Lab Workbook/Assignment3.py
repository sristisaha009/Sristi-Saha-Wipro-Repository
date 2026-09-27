from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    print("Registration page opened.")

    #select checkboxes
    sports_checkbox = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[text()='Sports']")
        )
    )

    sports_checkbox.click()
    sports_input = driver.find_element(
        By.ID, "hobbies-checkbox-1"
    )
    print("Sports selected:",sports_input.is_selected())

    reading_checkbox = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[text()='Reading']")
        )
    )
    reading_checkbox.click()
    reading_input = driver.find_element(
        By.ID, "hobbies-checkbox-2"
    )
    print("Reading selected:", reading_input.is_selected())

    assert sports_input.is_selected(), \
        "Sports checkbox was not selected."

    assert reading_input.is_selected(), \
        "Reading checkbox was not selected."

    # autocomplete dropdown
    subject_input = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "subjectsInput")
        )
    )

    subject_input.send_keys("Math")
    print("Typed 'Math' into autocomplete field.")

    wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                ".subjects-auto-complete__option"
            )
        )
    )

    suggestions = driver.find_elements(
        By.CSS_SELECTOR,
        ".subjects-auto-complete__option"
    )
    print("Suggestions found:")
    target_option = "Maths"
    for suggestion in suggestions:
        suggestion_text = suggestion.text.strip()
        print("-", suggestion_text)
        if suggestion_text == target_option:
            suggestion.click()
            print(
                "Matching option selected:",
                suggestion_text
            )
            break
    else:
        raise Exception(
            f"Autocomplete option '{target_option}' "
            f"was not found."
        )
    print("Assignment 3 PASSED")

finally:
    driver.quit()