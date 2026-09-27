import time
import pytest
from framework.config_reader import ConfigReader
from framework.driver_factory import DriverFactory
from framework.screenshot_util import ScreenshotUtil

@pytest.fixture
def driver(request):
    config = ConfigReader()
    web_driver = DriverFactory.create_driver()
    request.node._selenium_driver = web_driver
    yield web_driver
    pause = config.get_int(
        "application", "pause_after_test", 7
    )
    if pause > 0:
        print(f"\nKeeping browser open for {pause} seconds...")
        time.sleep(pause)
    web_driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        web_driver = getattr(
            item, "_selenium_driver", None
        )
        if web_driver:
            path = ScreenshotUtil.capture(
                web_driver, item.name
            )
            if path:
                try:
                    import pytest_html
                    extras = getattr(report, "extras", [])
                    extras.append(
                        pytest_html.extras.image(
                            path,
                            name="Failure screenshot"
                        )
                    )
                    report.extras = extras
                except Exception:
                    pass