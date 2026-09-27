from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Locate the Book Table
table = driver.find_element(
    By.CSS_SELECTOR,
    "table[name='BookTable']"
)

# Locate rows that are direct children of tbody
rows = table.find_elements(
    By.CSS_SELECTOR,
    "tbody > tr"
)

print("Number of rows found:", len(rows))

# Interact with the first data row
first_row = rows[1]

cells = first_row.find_elements(
    By.CSS_SELECTOR,
    "td"
)

print("Book:", cells[0].text)
print("Author:", cells[1].text)
print("Price:", cells[3].text)

time.sleep(3)

driver.quit()