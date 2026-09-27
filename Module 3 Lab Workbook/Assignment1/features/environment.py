from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        input("\nPress ENTER to close the browser...")
        context.driver.quit()