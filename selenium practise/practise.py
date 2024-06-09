from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_and_close_tabs():
    driver = webdriver.Chrome()
    driver.get("https://docs.python.org/3/tutorial/")  

    # Find all the links in the left navigation menu
    nav_links = driver.find_elements(By.XPATH, "//li[@class='toctree-l1']/a")

    # Open all links in new tabs
    for link in nav_links:
        url = link.get_attribute("href")
        driver.execute_script("window.open('" + url + "', '_blank');")
        
    # Get all the open window handles
    window_handles = driver.window_handles
    time.sleep(5)
    
    # Switch to the 5th window (index 4 since index starts from 0)
    driver.switch_to.window(window_handles[4])
    
    # Now you can perform actions on the 5th window
    print("Currently working in the 5th window:", driver.title)
    
    # Example: Click on a specific element in the 5th window
    # driver.find_element(By.XPATH,"//span[text()='Your Element']").click()
    
    # Close the browser session
    driver.quit()

# Call the function to open links and handle tabs
open_and_close_tabs()
