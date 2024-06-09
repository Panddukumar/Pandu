from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pynput.keyboard import Controller,Key




# Initialize the Chrome driver 
driver = webdriver.Chrome()

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

# clicking on 'ADD' attachment
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()

# clciking on 'browse' button
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-upload oxd-file-input-icon']").click()

# uploading a file
keyboard=Controller()
keyboard.type("C:\\Users\\tika-btm-ltp158\\Desktop\\Selenium-in-DDT.xlsx")
keyboard.press(Key.enter)
keyboard.release(Key.enter)



# Add an additional sleep to ensure the upload completes
time.sleep(10)

# Close the browser
driver.quit()
