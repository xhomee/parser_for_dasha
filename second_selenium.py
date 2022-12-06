# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get('https://ukrcomexpo.com/pharmacy_summit_Ukraine-2022/?token=83baf32a6cd2d471e1c389e1ffc511ec90cc5be7')
#
# element = driver.find_element(By.TAG_NAME, 'video')
#
# print(element.text)
# driver.close()




# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# #initialize web driver
# with webdriver.Chrome() as driver:
#     #navigate to the url
#     driver.get('https://ukrcomexpo.com/pharmacy_summit_Ukraine-2022/?token=83baf32a6cd2d471e1c389e1ffc511ec90cc5be7')
#     #find elements by tag name
#     elements = driver.find_elements(By.TAG_NAME, 'row')
#     for element in elements:
#         print(element.get_attribute("outerHTML"))

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/local/bin/chromedriver")
#initialize web driver
with webdriver.Chrome() as driver:
    #navigate to the url
    driver.get('https://ukrcomexpo.com/pharmacy_summit_Ukraine-2022/?token=83baf32a6cd2d471e1c389e1ffc511ec90cc5be7')
    #find element by tag name
    myDiv = driver.find_element(By.TAG_NAME, 'video')
    print(myDiv.get_attribute("outerHTML"))

