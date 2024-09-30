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

# Set up the Chrome driver using webdriver_manager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the webpage
url = "https://hk.on.cc/hk/bkn/cnt/news/20240928/bkn-20240928060109894-0928_00822_001.html"
driver.get(url)

try:
    # Wait for the image to be present in the DOM
    img_selector = "img[src='/hk/bkn/cnt/news/20240928/photo/bkn-20240928060109894-0928_00822_001_01p.jpg?20240928103713']"
    img_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, img_selector))
    )

    # Get the image location and size
    location = img_element.location
    size = img_element.size

    # Take a screenshot of the entire page
    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))

    # Calculate the boundaries of the image
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    # Crop the screenshot to get only the image
    image = screenshot.crop((left, top, right, bottom))

    # Save the image
    save_path = "/Users/minkeihon/Desktop/selenium/news_image.jpg"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    image.save(save_path)
    print(f"Image saved successfully to {save_path}")

except Exception as e:
    print(f"An error occurred: {e}")

    
time.sleep(3)
driver.close()