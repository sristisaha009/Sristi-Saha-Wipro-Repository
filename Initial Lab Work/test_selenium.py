from selenium import webdriver
driver = webdriver.Chrome()

try:
    driver.get("https://example.com")

    print("Page Title:",driver.title)
    print("Current URL:", driver.current_url)

finally:
    driver.quit()