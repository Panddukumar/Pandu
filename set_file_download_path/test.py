from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_option = Options()
prefs = {"download.default_directory": "C:\\Users\\tika-btm-ltp158\\Desktop\\test.png"}
chrome_option.add_experimental_option("prefs", prefs)

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=chrome_option)

# Navigate to the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)

# Login to the application
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Navigate to the 'My Info' section
driver.find_element(By.XPATH, "//span[text()='My Info']").click()
time.sleep(5)  # Allow some time for the page to load

# Locate and click the download button (assuming it's available)
# Replace with the correct XPATH or element identifier as needed
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-download']").click()

# Add an additional sleep to ensure the download completes
time.sleep(10)

# Close the browser
driver.quit()
