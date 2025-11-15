from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Valid credentials test
driver.find_element(By.ID, "username").send_keys("testuser")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "loginBtn").click()
time.sleep(2)
if "Dashboard" in driver.title:
    print("Test Passed: Valid credentials")
else:
    print("Test Failed: Valid credentials")

# Invalid credentials test
driver.get("https://example.com/login")
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "loginBtn").click()
time.sleep(2)
if "Invalid username or password" in driver.page_source:
    print("Test Passed: Invalid credentials")
else:
    print("Test Failed: Invalid credentials")

driver.quit()
