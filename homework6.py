from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from PIL import Image
from io import BytesIO
import requests

# Set up the Chrome driver using webdriver_manager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the webpage
url = "https://hk.on.cc/hk/bkn/cnt/news/20240928/bkn-20240928130520134-0928_00822_001.html"
driver.get(url)

try:
    # Wait for the headline to be present in the DOM
    headline_selector = "div[class='topHeadline'] h1"
    headline_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, headline_selector))
    )
    
    # Get the headline text
    headline_text = headline_element.text
    print(f"Headline: {headline_text}")

    # Wait for the image to be present in the DOM
    img_selector = "div[class='photo hPhoto'] div:nth-child(1) div:nth-child(1) img:nth-child(1)"
    img_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, img_selector))
    )

    # Get the image source URL
    img_src = img_element.get_attribute('src')
    
    # Download the image
    img_data = requests.get(img_src).content
    
    # Save the image
    save_path = "/Users/minkeihon/Desktop/selenium/news_image.jpg"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, 'wb') as handler:
        handler.write(img_data)
    print(f"Image saved successfully to {save_path}")

except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(3)
driver.close()