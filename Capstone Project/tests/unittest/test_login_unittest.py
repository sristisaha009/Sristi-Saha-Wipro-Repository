import unittest
import time
from framework.config_reader import ConfigReader
from framework.driver_factory import DriverFactory
from framework.screenshot_util import ScreenshotUtil
from pages.login_page import LoginPage

class LoginUnittest(unittest.TestCase):
    def setUp(self):
        self.config = ConfigReader()
        self.driver = DriverFactory.create_driver()

    def tearDown(self):
        if getattr(self, "driver", None):
            pause = self.config.get_int(
                "application", "pause_after_test", 7
            )
            if pause > 0:
                print(
                    f"\nKeeping browser open for {pause} seconds..."
                )
                time.sleep(pause)
            self.driver.quit()

    def test_invalid_login_displays_warning(self):
        try:
            page = LoginPage(self.driver).open(
                self.config.get("application", "base_url")
            )
            page.login(
                "invalid@example.com",
                "IncorrectPassword123"
            )
            self.assertTrue(
                page.is_visible(page.WARNING),
                "Invalid login warning was not visible."
            )
            self.assertTrue(
                page.warning_text().strip(),
                "Login warning message was empty."
            )

        except Exception:
            # Capture screenshot before the browser is closed.
            ScreenshotUtil.capture(
                self.driver,
                self._testMethodName
            )
            raise

if __name__ == "__main__":
    unittest.main(verbosity=2)