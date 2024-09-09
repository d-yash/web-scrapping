from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys


driver = webdriver.Chrome()

url = "https://www.overstock.com/collections/furniture?brand=%5B%22Signature+Design+by+Ashley%22%5D"
driver.get(url)
time.sleep(3) 

products = driver.find_elements(By.CLASS_NAME, '_productCard_tt671_14')

for product in products:
    try:
        prod = {}
        url = product.get_attribute('href')
        name = product.find_element(By.XPATH, ".//span[contains(@class, '_title_tt671_1')]").text
        price = product.find_element(By.XPATH, ".//div[contains(@class, '_price_pvbau_1')]").text
        
        driver.get(url)
        brand = driver.find_element(By.XPATH, ".//span[contains(@class, 'product-vendor')]/a").text
        sku = driver.find_element(By.XPATH, ".//span[contains(@class, 'product-sku')]/span[contains(@class, 'product-sku__value')]").text
        # print(sku)
        # print(brand)
        prod['name'] = name
        prod['brand'] = brand
        prod['sku'] = sku
        prod['url'] = url

        print(prod)
        break
    except Exception as e:
        print(f"Error extracting data: {e}")

driver.quit()
