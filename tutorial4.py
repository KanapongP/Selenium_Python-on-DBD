from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


PATH = "C:/Users/Asus/Desktop/temp/selenium/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie  = driver.find_element_by_id("bigCookie")
count = driver.find_element_by_id("cookies")
item = [driver.find_element_by_id(" ")]

actions = ActionChains(driver)
actions.click()