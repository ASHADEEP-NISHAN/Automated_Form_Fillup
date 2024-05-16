from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program finish
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

# crete and configure web driver
driver=webdriver.Chrome(options=chrome_option)

driver.get(url="http://secure-retreat-92358.herokuapp.com/")

first_name=driver.find_element(By.NAME,value="fName")
first_name.send_keys("Ashadeep")

last_name=driver.find_element(By.NAME,value="lName")
last_name.send_keys("Sahoo")

email=driver.find_element(By.NAME,value="email")
email.send_keys("kadali@gmail.com")

button=driver.find_element(By.CSS_SELECTOR,".form-signin button")
button.click()