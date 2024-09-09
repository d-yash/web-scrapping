from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
from pprint import pprint

sys.stdout.reconfigure(encoding='utf-8')

driver = webdriver.Chrome()

driver.get(f"https://www.flipkart.com/search?q=seiko%20watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

time.sleep(2)

container = driver.find_elements(By.CLASS_NAME, 'hCKiGj')   #product container element
brand_products = {}

for product in container:
    try:
        brand_element = product.find_element(By.CLASS_NAME, 'syl9yP')
        name_element  = product.find_element(By.CLASS_NAME, 'WKTcLC') 
        price_element = product.find_element(By.CLASS_NAME, 'Nx9bqj')

        brand = brand_element.text
        name = name_element.get_attribute("title")
        price = price_element.text

        if brand not in brand_products:
            brand_products[brand] = []
        brand_products[brand].append({name: price})
    except Exception as e:
        print(f"Error extracting data: {e}")

pprint(brand_products, indent=4)


input("Press Enter to close the browser and exit...")
driver.close()