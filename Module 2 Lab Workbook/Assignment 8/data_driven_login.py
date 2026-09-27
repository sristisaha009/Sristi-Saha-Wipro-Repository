import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from login_page import LoginPage

with open("test_data.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_case = row["test_case"]
        username = row["username"]
        password = row["password"]
        expected_result = row["expected_result"]
        expected_error = row["expected_error"]

        print("\n----------------------------------------")
        print("Running:", test_case)
        print("Username:", username)
        print("Expected Result:", expected_result)

        driver = webdriver.Chrome()
        try:
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            # Wait until page is completely loaded
            WebDriverWait(driver, 15).until(
                lambda d: d.execute_script(
                    "return document.readyState"
                ) == "complete"
            )
            print("Page Title:", driver.title)
            print("Current URL:", driver.current_url)
            login_page = LoginPage(driver)
            login_page.login(username, password)

            if expected_result == "success":
                assert "inventory" in driver.current_url, \
                    "User was not redirected to the inventory page."
                print("RESULT: PASS")

            elif expected_result == "error":
                actual_error = login_page.get_error_message()
                assert expected_error in actual_error, \
                    f"Expected: {expected_error}\nActual: {actual_error}"
                print("RESULT: PASS")
                print("Actual Error:", actual_error)

        except AssertionError as e:
            print("RESULT: FAIL")
            print("Assertion Error:", e)
        except Exception as e:
            print("RESULT: FAIL")
            print("Unexpected Error:", type(e).__name__)
            print("Error Details:", e)

        finally:
            driver.quit()

print("\n========================================")
print("DATA-DRIVEN TESTING COMPLETED")
print("========================================")