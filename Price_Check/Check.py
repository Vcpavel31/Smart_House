import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


data = {"url": "https://e3d-online.com/products/revo-hemera", "to_click": ['//*[@id="configurator"]/ul/li[1]/ul/li[2]'], "read": "/html/body/main/div[2]/section[1]/div/div[2]/div/div[1]/span"}


def GBP(browser, read):
    browser.get("https://www.csas.cz/cs/kurzovni-listek#/type/NONCASH/from/CZK/to/GBP")
    #browser.find_element(By.XPATH, '//*[@id="popin_tc_privacy_button"]').click()
    browser.find_element(By.XPATH, '//*[@id="conversion-to"]').send_keys(str(read))
    print(browser.find_element(By.XPATH, '//*[@id="conversion-from"]').text)

print(data["url"])

browser = webdriver.Chrome()
browser.get(data["url"])
for xpath in data["to_click"]:
    browser.find_element(By.XPATH, xpath).click()
read = (browser.find_element(By.XPATH, data["read"]).text)

if("£" in read):
    GBP(browser, float(read.replace("£", "").split(" ")[0]))
