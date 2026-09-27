import pytest
from pathlib import Path
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screenshot_path = screenshot_dir / f"{item.name}.png"
            driver.save_screenshot(str(screenshot_path))
            print(f"\nScreenshot saved: {screenshot_path}")
            pytest_html = item.config.pluginmanager.getplugin("html")

            if pytest_html:
                extra = getattr(report, "extras", [])
                extra.append(pytest_html.extras.image(str(screenshot_path)))
                report.extras = extra
