from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # Launch Chrome browser
driver.get("https://docs.python.org/3/tutorial/") 

nav_links = driver.find_elements(By.XPATH, "//li[@class='toctree-l1']/a")

# Open only odd-numbered links in new tabs
for i in range(len(nav_links)):
    if i % 2 != 0:  # Check if the index is odd
        link = nav_links[i]
        url = link.get_attribute("href")
        
        # Print the title of the page
        driver.execute_script("window.open('"+url+"', '_blank');")
        time.sleep(2)  # Wait for the new tab to open
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the new tab
        title = driver.title  # Get the title of the page
        print("Title:", title)  # Print the title
        driver.close()  # Close the new tab
        driver.switch_to.window(driver.window_handles[0])  # Switch back to the main tab (home page)

# Close the browser
driver.quit()
