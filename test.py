from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import xlrd
import csv


PATH = "C:/Users/Asus/Desktop/temp/selenium/chromedriver.exe"
FPATH = "C:/Users/Asus/Desktop/temp/selenium/Client-List_A-B-C.xlsx"
driver = webdriver.Chrome(PATH)
wb = xlrd.open_workbook(FPATH)
sheet = wb.sheet_by_index(0)
file = open('result.csv', 'w')
officeData = '/html/body/div/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table/tbody/'
incomeLossPercent = '/html/body/div/div[4]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div/div/div[1]/div/div[1]/'
incomeLoss = '/html/body/div/div[4]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div/div/div[1]/div/div[2]/'


def scapingdata(start, end):
    for i in range(start, end):
        print(str(int(sheet.cell_value(i, 0))))
        code = str(int(sheet.cell_value(i, 0)))
        search = driver.find_element_by_name("textSearch")
        search.send_keys(code)
        element = driver.find_element_by_id("Capa_1")
        element.click()
        print("data show")
        data = driver.find_element_by_tag_name('tbody')
        data.click()
        print("click on result")
        data1 = driver.find_element_by_xpath(officeData+'tr[4]/td[2]')
        print(data1.text)
        data2 = driver.find_element_by_xpath(officeData+'tr[5]/td[2]')
        print(data2.text)
        data3 = driver.find_element_by_xpath(
            '/html/body/div/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[4]/div/p')
        print(data3.text)
        data4 = driver.find_element_by_xpath(
            incomeLossPercent+'div[1]/div/ul/li[3]/span[1]/span')
        print(data4.text)
        data5 = driver.find_element_by_xpath(
            incomeLossPercent+'div[2]/div/ul/li[3]/span[1]/span')
        print(data5.text)
        data6 = driver.find_element_by_xpath(
            incomeLoss+'div[1]/div/ul/li[3]/span[1]')
        print(data6.text)
        data7 = driver.find_element_by_xpath(
            incomeLoss+'div[2]/div/ul/li[2]/span[1]')
        print(data7.text)
        writer.writerow({'เลขทะเบียนนิติบุคคล': code, 'วันที่จดทะเบียนจัดตั้ง': data1.text, 'ทุนจดทะเบียน': data2.text, 'ประเภทธุรกิจตอนจดทะเบียน': data3.text[6:],
                         'รายได้รวม': data4.text, 'กำไรสุทธิ': data5.text, 'ค่ามัธยฐานของรายได้รวม': data6.text, 'ค่ามัธยฐานของกำไรสุทธิ': data7.text})
        driver.find_element_by_name("textSearch").clear()
        print("go to result page")


def WaitForCap():
    search = driver.find_element_by_name("textSearch")
    search.send_keys("asdfg")
    element = driver.find_element_by_id("Capa_1")
    element.click()
    time.sleep(25)
    driver.find_element_by_name("textSearch").clear()


driver.get("https://datawarehouse.dbd.go.th")
driver.maximize_window()
WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.ID, "textStr")))
try:
    # try to use any method
    print("go to ju page")
    choice = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "ค้นหาข้อมูลนิติบุคคล และแสดงรายละเอียดของนิติบุคคล เช่น สถานะ ที่ตั้ง ประวัติการเปลี่ยนแปลง ทุนจดทะเบียน เป็นต้น"))
    )
    with file:
        header = ['เลขทะเบียนนิติบุคคล', 'วันที่จดทะเบียนจัดตั้ง', 'ทุนจดทะเบียน', 'ประเภทธุรกิจตอนจดทะเบียน',
                  'รายได้รวม', 'กำไรสุทธิ', 'ค่ามัธยฐานของรายได้รวม', 'ค่ามัธยฐานของกำไรสุทธิ']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        choice.click()
        scapingdata(2, 12)
        WaitForCap()
        scapingdata(15, 25)
        WaitForCap()
        scapingdata(28, 38)
finally:
    print("done")
    driver.quit()