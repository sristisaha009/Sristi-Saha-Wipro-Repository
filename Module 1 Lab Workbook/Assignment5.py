from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://the-internet.herokuapp.com/tables")
    driver.maximize_window()
    print("Web table page opened.")

    #locate table
    table = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "table1")
        )
    )

    # read table headers
    headers = table.find_elements(
        By.CSS_SELECTOR,
        "thead th"
    )

    header_names = []

    for header in headers:
        header_names.append(header.text.strip())

    print("\nTable Headers:")
    print(header_names)

    # read all rows
    rows = table.find_elements(
        By.CSS_SELECTOR,
        "tbody tr"
    )

    print("\nTable Data:")

    for row in rows:
        columns = row.find_elements(
            By.TAG_NAME,
            "td"
        )

        row_data = []

        for column in columns:
            row_data.append(column.text.strip())

        print(row_data)

    # find specific person
    target_name = "Smith"
    target_due = None

    for row in rows:
        columns = row.find_elements(
            By.TAG_NAME,
            "td"
        )

        last_name = columns[0].text.strip()

        if last_name == target_name:
            target_due = columns[3].text.strip()
            break

    if target_due is not None:
        print("\nTarget person found:", target_name)
        print("Due value:", target_due)

    else:
        print("\nPerson not found:", target_name)
        print("Assignment 5 PASSED")

finally:
    driver.quit()