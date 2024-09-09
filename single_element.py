from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# query = "mobile"
# driver.get(f"https://www.amazon.in/s?k={query}&crid=1PE5XAZHEW73R&sprefix=mobil%2Caps%2C200&ref=nb_sb_noss_2")
# product_name = driver.find_element(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a/span")
# print(product_name.text)

driver.get(f"https://www.flipkart.com/search?q=watches+for+men&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DCASIO")

time.sleep(5)

watch_name = driver.find_elements(By.CLASS_NAME, "WKTcLC")
price = driver.find_elements(By.CLASS_NAME, 'Nx9bqj')

watch_list = []

for watch in watch_name:
    full_name =  watch.get_attribute("title")
    if(full_name):
        watch_list.append(full_name)


print("\n".join(watch_list))


driver.close()