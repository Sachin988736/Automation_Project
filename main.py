import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyperclip
import re
from datetime import datetime
# import datetime

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("")

# driver.find_element(By.XPATH, " //input[@placeholder='Find by Name/Category']").send_keys("test")
# time.sleep(6)
# # driver.switch_to.frame()
# result = driver.find_elements(By.XPATH, "//div[@id = 'ej2_dropdownlist_0_popup']")
# print(result)
# new = []
# for name in result:
#     new = name.text
# print(new)

# ABOUTUS = (By.XPATH, "(//a[text()='About'])[1]")
#
# about_element = driver.find_element(By.XPATH, "(//a[text()='About'])[1]")
# action = ActionChains(driver)
# action.move_to_element(about_element).perform()
#
# time.sleep(8)
#
# # Get the text from the clipboard
# clipboard_text = pyperclip.paste()
#
# # Print the clipboard text
# print("Clipboard text:", clipboard_text)

# original_string = "This is an (dynamic wasdorld)"
# result_string = re.sub(r'\([^)]*\)', '', original_string).strip()
# print(result_string)


# EXP_Name = "test auto " + datetime.datetime.now().strftime("%H%M%S%B%d%Y")
# print(EXP_Name)
# ab = [3, 4, 55, 55]
# b = 553
# assert b in ab
# print("b  in list")
now = datetime.now()
today = "98899"
print(type(today))
str_value_without_zeros = today.lstrip('0')
print(str_value_without_zeros)
driver.switch_to.default_content()
