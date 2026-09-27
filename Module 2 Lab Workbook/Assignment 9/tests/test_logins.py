from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(
        "standard_user",
        "secret_sauce"
    )
    assert "inventory" in driver.current_url

def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.login(
        "wrong_user",
        "secret_sauce"
    )
    error = login_page.get_error_message()
    assert "Username and password do not match" in error

def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.login(
        "standard_user",
        "wrong_password"
    )
    error = login_page.get_error_message()
    assert "Username and password do not match" in error

def test_intentional_failure_for_screenshot(driver):
    """
    Intentionally fails so one execution contains both PASS and FAIL.
    The failure triggers the screenshot hook in conftest.py.
    """
    login_page = LoginPage(driver)
    login_page.login(
        "standard_user",
        "secret_sauce"
    )
    assert "THIS_PAGE_DOES_NOT_EXIST" in driver.current_url
