from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://202.85.216.21:8095/review")
time.sleep(2)
# username = "1879440982@qq.com"
# userpassword = "Netmarch@123"
username = "21242705@qq.com"
userpassword = "1qaz@WSX"
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div/input').send_keys(userpassword)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/div/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="clearText"]').click()
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div/form/div/div[2]/div[2]').send_keys(lines)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="correctText"]').click()
lis = []
data_1 = driver.find_elements(By.XPATH, "//*[@id='spell_corrects']/div/div/div")
data_2 = driver.find_elements(By.XPATH, "//*[@id='grammar_corrects']/div/div/div")
print(len(data_1))
for i in range(len(data_1)):
    ad = i + 1
    lis.append(driver.find_element_by_xpath(
        '/html/body/div[5]/div[2]/div/div[2]/div/div[3]/div/div/div[' + str(ad) + ']').get_attribute('data-json'))
# for i in range(len(data_2)):
#    ad = i + 1
#   lis.append(driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/div/div[4]/div/div/div['+str(ad)+']').get_attribute('data-json'))
lis = list(set(lis))
li = []
for line in lis:
    li.append(line[1:-2].replace('\'', '').split(','))
print(li)
last = []
for i in range(len(lines)):
      for x in li:
        if i == int(x[1]) - 1:
            last.append('/error@' + x[3].replace(' ', '') + '/')
      last.append(lines[i])

file.writelines(last)
driver.close()
