from selenium import webdriver

PATH = "C:/Users/Asus/Desktop/temp/selenium/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()
