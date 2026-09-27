from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from framework.config_reader import ConfigReader

class DriverFactory:
    @staticmethod
    def create_driver():
        config = ConfigReader()
        browser = config.get("application", "browser", "chrome").strip().lower()
        headless = config.get_bool("application", "headless", False)

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--window-size=1440,1000")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            driver = webdriver.Firefox(options=options)
            driver.set_window_size(1440, 1000)
        else:
            raise ValueError(f"Unsupported browser '{browser}'. Use chrome or firefox.")

        driver.set_page_load_timeout(config.get_int("application", "page_load_timeout", 30))
        return driver
