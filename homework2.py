from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver
service = Service('./chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Navigate to Google.com
url = "https://www.google.com"
driver.get(url)

# Wait for the search input field to be present
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# Input "music" into the search field and submit
search_input.send_keys("jazz music")
search_input.send_keys(Keys.RETURN)

# Wait for a moment to see the results
time.sleep(3)

# Close the browser
driver.quit()