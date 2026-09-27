import pytest
from framework.config_reader import ConfigReader
from framework.data_reader import CSVDataReader
from pages.login_page import LoginPage

@pytest.mark.parametrize("row", CSVDataReader.read_rows("login_data.csv"))
def test_invalid_login_shows_validation_message(driver, row):
    config = ConfigReader()
    page = LoginPage(driver).open(config.get("application", "base_url"))
    page.login(row["email"], row["password"])
    assert page.is_visible(page.WARNING), "Expected an invalid-login warning to be displayed."
    assert "warning" in page.warning_text().lower() or "no match" in page.warning_text().lower()
