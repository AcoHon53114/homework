from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)
url = "https://hk.on.cc/hk/bkn/cnt/news/20240928/bkn-20240928060109894-0928_00822_001.html"
driver.get(url)
search = driver.find_element(by=By.CSS_SELECTOR, value="div[class='topHeadline'] h1").text
search1 = driver.find_element(by=By.CSS_SELECTOR, value="div[class='paragraph']").text
para = driver.find_element(By.XPATH, ("(//div[@class='paragraph'])")).text
print(search, search1)
print(para)
time.sleep(3)
driver.close()