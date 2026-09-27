from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    #iframe
    driver.get(
        "https://the-internet.herokuapp.com/iframe"
    )
    driver.maximize_window()
    print("Iframe page opened.")

    iframe = wait.until(
        EC.presence_of_element_located(
            (By.ID, "mce_0_ifr")
        )
    )

    driver.switch_to.frame(iframe)
    print("Switched into iframe.")
    editor = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "tinymce")
        )
    )

    editor.click()
    editor.send_keys(
        Keys.CONTROL,
        "a"
    )
    editor.send_keys(
        Keys.BACKSPACE
    )

    editor.send_keys(
        "Hello from Selenium!"
    )

    print("Text entered inside iframe.")

    driver.switch_to.default_content()

    print("Switched back to main page.")

    # new tab/window
    driver.get(
        "https://the-internet.herokuapp.com/windows"
    )
    print("\nWindows page opened.")

    original_window = driver.current_window_handle

    new_window_button = wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Click Here")
        )
    )

    new_window_button.click()
    wait.until(
        EC.number_of_windows_to_be(2)
    )

    windows = driver.window_handles
    print(
        "Number of windows:",
        len(windows)
    )

    for window in windows:
        if window != original_window:
            driver.switch_to.window(window)
            break

    new_window_title = driver.title

    print("New window title:", new_window_title)

    driver.close()
    print("New window closed.")

    driver.switch_to.window(
        original_window
    )

    print("Switched back to original window.")
    print("\nAssignment 6 PASSED")

finally:
    input("Press enter to exit")
    driver.quit()