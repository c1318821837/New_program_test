from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

username = sys.argv[1]
driver = webdriver.Firefox()
driver.get("https://home.firefoxchina.cn/")
time.sleep(2)
print(username)
driver.close()
