from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)

# Locate the element whose background color you want to verify
element = driver.find_element(By.XPATH, "//button[@type='submit']")

# Retrieve the background color property
color = element.value_of_css_property("background-color")
print(color)

# Close the WebDriver
driver.quit()
