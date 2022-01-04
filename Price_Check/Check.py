import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

import csv

datas = [{"url": "https://e3d-online.com/products/revo-hemera", "to_click": ['//*[@id="configurator"]/ul/li[1]/ul/li[2]'], "read": '/html/body/main/div[2]/section[1]/div/div[2]/div/div[1]/span'},
         {"url": "https://eu.store.ui.com/products/unifi-6-long-range-access-point-1", "to_click": [], "read": '//*[@id="bundleApp"]/div[2]/div[1]/div[1]/div[2]'},
         {"url": "https://eu.store.ui.com/collections/unifi-network-routing-switching/products/usw-flex", "to_click": [], "read": '//*[@id="bundleSlider"]/li[1]/div[2]/div[1]/div[4]/div[2]/div'},
         {"url": "https://eu.store.ui.com/collections/unifi-network-routing-switching/products/usw-flex-mini", "to_click": [], "read": '//*[@id="bundleApp"]/div[2]/div[1]/div[1]/div[2]'}]

def GetFloat(price_arr):
    for x in price_arr:
        try:
            x = str(x).replace(",", ".")
            float(x)
            return x
        except: pass
    return 0


Kurzy = json.loads("{}")
with open('export.csv', newline='', encoding='utf-8') as csvfile:
    i = 0
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for rows in spamreader:
        if(i != 0):
            Kurzy[rows[1]] = json.loads('{"Datum": "'+str(rows[0])+'", "Nakup_Hotovost": "'+str(rows[4])+'", "Prodej_Hotovost": "'+str(rows[5])+'", "Stred_Hotovost": "'+str(rows[6])+'", "Nakup_Online": "'+str(rows[7])+'", "Prodej_Online": "'+str(rows[8])+'", "Stred_Online": "'+str(rows[9])+'", "Stred_CNB": "'+str(rows[10])+'", "Zmena": "'+str(rows[11])+'", "Stred_ECB": "'+str(rows[12])+'"}')
        else: i = 1

print(json.dumps(Kurzy, indent=4, sort_keys=True))

browser = webdriver.Chrome()

for data in datas:
    #print(data["url"])
    browser.get(data["url"])
    if(data["to_click"] != []):
        for xpath in data["to_click"]:
            browser.find_element(By.XPATH, xpath).click()
    read = (browser.find_element(By.XPATH, data["read"]).text)
    
    if("£" in read or "GBP" in read):
        price_arr = read.replace("£", "").replace("GBP", "").split(" ")
        price = GetFloat(price_arr)
        cena = float(price)*float(Kurzy["GBP"]["Prodej_Online"])
    elif("$" in read or "USD" in read):
        price_arr = read.replace("$", "").replace("USD", "").split(" ")
        price = GetFloat(price_arr)
        cena = float(price)*float(Kurzy["USD"]["Prodej_Online"])
    elif("€" in read or "EUR" in read or "EURO" in read):
        price_arr = read.replace("€", "").replace("EUR", "").replace("EURO", "").split(" ")
        price = GetFloat(price_arr)
        cena = float(price)*float(Kurzy["USD"]["Prodej_Online"])
    else:
        print(read)
    print(str(data["url"])+" >> "+str(round(cena,2))+" Kč")

browser.close()
