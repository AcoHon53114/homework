from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the webdriver (Chrome in this example)
driver = webdriver.Chrome()

try:
    # Visit Google.com
    driver.get("https://www.google.com")

    # Find the search box and input "news"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("news")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    # Find and click the first search result link
    first_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#search .g a"))
    )
    first_result.click()

    # Wait for the new page to load (you can adjust the wait time if needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    print("Successfully navigated to the first news result.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()