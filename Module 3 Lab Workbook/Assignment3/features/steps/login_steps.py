from behave import given, when, then
from pages.login_page import LoginPage

@given("I open the Sauce Demo login page")
def open_login_page(context):
    context.login_page = LoginPage(
        context.driver
    )
    context.login_page.open()
    print("Sauce Demo login page opened")
    input("Press ENTER.")

@when('I enter username "{username}"')
def enter_username(context, username):
    context.login_page.enter_username(
        username
    )
    print("Username entered:", username)

@when('I enter password "{password}"')
def enter_password(context, password):
    context.login_page.enter_password(
        password
    )
    print("Password entered")
    input(" Press ENTER.")


@when("I click the login button")
def click_login(context):
    context.login_page.click_login()
    print("Login button clicked")

@then("I should be redirected to the inventory page")
def verify_successful_login(context):
    assert context.login_page.is_inventory_displayed()
    print("PASS: Inventory page displayed")
    print("Current URL:", context.driver.current_url)
    input(" Press ENTER.")

@then("I should see the login error message")
def verify_login_error(context):
    error = context.login_page.get_error_message()
    assert "Username and password do not match" in error
    print("PASS: Invalid login correctly rejected")
    print("Error message:", error)
    input("Press ENTER.")