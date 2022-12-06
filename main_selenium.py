# #pip install selenium
# import selenium
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("https://ukrcomexpo.com/pharmacy_summit_Ukraine-2022/?token=b24c65985c3d63aef6eacd17a0c7b2d9c3357199")
# assert "Аптечний саміт" in driver.title
# #elem = driver.find_element_by_name("a")
# elem = driver.find_element_by_id('video')
# #elem.send_keys("pycon")
# #elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()



from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib3

driver = webdriver.Chrome()
driver.get("https://ukrcomexpo.com/pharmacy_summit_Ukraine-2022/?token=34997651c3959fefa205e27b47315434e2ef04bf")

    # Get element with tag name 'div'
element = driver.find_element(By.TAG_NAME, 'div')

    # Get all the elements available with tag name 'p'
elements = element.find_elements(By.TAG_NAME, 'class')
for e in elements:
    print(e.text)

vegetable = driver.find_element(By.CLASS_NAME, "bg-main main-card")
print(vegetable)

