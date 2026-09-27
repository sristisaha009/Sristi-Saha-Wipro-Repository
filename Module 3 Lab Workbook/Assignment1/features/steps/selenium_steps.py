from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I open the DemoQA text box page")
def open_page(context):
    context.driver.get(
        "https://demoqa.com/text-box"
    )
    print("Opened DemoQA Text Box page")
    input("Press ENTER to continue.")


@when("I enter my name, email and address")
def enter_details(context):
    driver = context.driver
    driver.find_element(
        By.ID, "userName"
    ).send_keys("Sristi Saha")

    driver.find_element(
        By.ID, "userEmail"
    ).send_keys("sristi@example.com")
    driver.find_element(
        By.ID, "currentAddress"
    ).send_keys("Kolkata, India")

    driver.find_element(
        By.ID, "permanentAddress"
    ).send_keys("West Bengal, India")
    print("Form details entered successfully")
    input("Press ENTER to continue.")

@when("I submit the form")
def submit_form(context):
    driver = context.driver
    driver.find_element(
        By.ID, "submit"
    ).click()
    print("Form submitted")

@then("I should see the submitted details")
def verify_details(context):
    driver = context.driver
    output = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "output")
        )
    )
    assert "Sristi Saha" in output.text
    assert "sristi@example.com" in output.text
    assert "Kolkata, India" in output.text
    print("PASS: Submitted details verified")
    input(" Press ENTER.")