from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#  ^=  is  attribute value STARTS WITH
starts_with = driver.find_elements(
    By.CSS_SELECTOR,
    "input[id^='input']"
)
print("Elements whose ID starts with 'input':")
for element in starts_with:
    print("ID:", element.get_attribute("id"))


# $=  is  attribute value ENDS WITH
ends_with = driver.find_elements(
    By.CSS_SELECTOR,
    "input[id$='name']"
)
print("\nElements whose ID ends with 'name':")
for element in ends_with:
    print("ID:", element.get_attribute("id"))


# *=  is  attribute value CONTAINS
contains = driver.find_elements(
    By.CSS_SELECTOR,
    "input[id*='name']"
)
print("\nElements whose ID contains 'name':")
for element in contains:
    print("ID:", element.get_attribute("id"))

time.sleep(3)
driver.quit()