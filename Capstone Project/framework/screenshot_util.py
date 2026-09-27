from datetime import datetime
from pathlib import Path
from framework.config_reader import ConfigReader, PROJECT_ROOT

class ScreenshotUtil:
    @staticmethod
    def capture(driver, test_name):
        config = ConfigReader()
        directory = PROJECT_ROOT / config.get("reporting", "screenshot_dir", "screenshots")
        directory.mkdir(parents=True, exist_ok=True)
        safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in test_name)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = directory / f"{safe_name}_{timestamp}.png"
        if driver:
            driver.save_screenshot(str(path))
            return str(path)
        return None
