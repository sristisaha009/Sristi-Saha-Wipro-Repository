from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://books.toscrape.com/")
    driver.maximize_window()

    print("Website opened successfully.")
    print("First five books found:")

    books = driver.find_elements(
        By.CSS_SELECTOR,
        "article.product_pod"
    )[:5]

    for index, book in enumerate(books, start=1):
        title = book.find_element(
            By.CSS_SELECTOR,
            "h3 a"
        ).get_attribute("title")

        price = book.find_element(
            By.CSS_SELECTOR,
            "p.price_color"
        ).text

        print(f"{index}. {title} - {price}")
    print("Automation completed successfully.")

finally:
    time.sleep(7)
    driver.quit()