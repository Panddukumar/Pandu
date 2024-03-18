from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_odd_links_in_new_window():
    driver = webdriver.Chrome()  # Launch Chrome browser
    driver.get("https://docs.python.org/3/tutorial/")  # Navigate to the Tutorials section on the Python official website

    # Find all the links in the left navigation menu
    nav_links = driver.find_elements(By.XPATH,"//li[@class='toctree-l1']/a")

    # Open only odd-numbered links in new tabs
    for i in range(len(nav_links)):
        if (i%2)== 0:  # Check if the index is odd
            link = nav_links[i]
            link_text = link.text

            # Open the link in a new tab
            driver.execute_script("window.open('" + link.get_attribute("href") + "', '_blank');")
            time.sleep(2)  # Wait for new tab to open
            
            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[-1])

            # Print the title of the opened page
            print("Opened:", link_text)

            # Close the current tab
            driver.close()

            # Switch back to the main tab
            driver.switch_to.window(driver.window_handles[0])

            time.sleep(2)  # Wait for main tab to become active

    # Close the browser session
    driver.quit()

# Call the function to open odd-numbered links in new windows
open_odd_links_in_new_window()
