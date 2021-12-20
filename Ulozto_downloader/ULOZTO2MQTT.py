import sys
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import paho.mqtt.client as paho

from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, 
                             QMessageBox, QPushButton, QVBoxLayout, 
                             QWidget, QLineEdit)

def Key(name):
    if(name == "The Flash (2014)"):
        return "The Flash"
    else:
        if(name == "The Grand Tour (2016)"):
            return "The Grand Tour"
        else:
            return name

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        layout = QVBoxLayout()
        self.widget.setLayout(layout)

        self.button = QPushButton(parent=self, text="Start")
        self.button.clicked.connect(self.button_clicked_kill)
        self.text = QLabel(parent=self, text='')

        layout.addWidget(self.button)
        layout.addWidget(self.text)

    def button_clicked_kill(self):
        headers={'x-api-key':'ff55d9d863ea4219bc87aa853ee074b3'}
        client = paho.Client("Ulozto_Generator_2")                      
        resp = requests.get("http://10.0.0.16:8989/api/missing/? -X GET",headers=headers)
        y = json.loads(resp.content)
        browser = webdriver.Chrome()
        browser.get('https://uloz.to/hledej?q=test&type=videos&orderby=rating')
        video = browser.find_element(By.XPATH, '//*[@id="js-search-filter"]/div[1]/ul/li[2]/a')
        video.click()
        sort = browser.find_element(By.XPATH, '//*[@id="js-search-filter"]/div[3]/div[1]/ul/li')
        sort.click()
        hodnoceni = browser.find_element(By.XPATH, '//*[@id="js-search-filter"]/div[3]/div[1]/ul/li/ul/li[3]/a')
        hodnoceni.click()
        assert "Ulož.to" in browser.title
        remeber = browser.find_element(By.XPATH, '//*[@id="rememberFilters"]')
        remeber.click()
        for x in y['records']:
    
            print(x["series"]["title"])
            name = Key(x["series"]["title"])
            url = "http://10.0.0.16:8989/api/v3/episode?seriesId="+str(x["seriesId"])
            resp = requests.get(url,headers=headers)
            y = json.loads(resp.content)
            
            for z in y:
                print(("S0" if (z["seasonNumber"]<10) else "S") +str(z["seasonNumber"])+("E0" if (z["episodeNumber"]<10) else "E")+str(z["episodeNumber"]),"=",z["hasFile"])
                if(z["hasFile"] == False): ## Dont search for already downloaded files
                    #if(z["seasonNumber"] >= 1): ##### Dont search for bonuses :D Becuse czech peoples ARE IDIOTS
                    if(z["monitored"] == True): ## Filter out not monitored serials 
                        print("Opening web browser.")
                        search = browser.find_element(By.XPATH, '//*[@id="search-input"]')
                        search.clear()
                        search.send_keys(str(name)+" "+("S0" if (z["seasonNumber"]<10) else "S") +str(z["seasonNumber"])+("E0" if (z["episodeNumber"]<10) else "E")+str(z["episodeNumber"])+" CZ")
                        client.connect("10.0.0.16",1883)
                        button = browser.find_element(By.XPATH, '//*[@id="search"]/button')
                        button.click()
                        self.Test(browser, client)
                        client.disconnect()
        browser.close()

    def wait(self):
        reply = QMessageBox.question(self, 'Downloader', 'Download link found?')
        if reply == QMessageBox.Yes:
            return 1
        if reply == QMessageBox.No:
            return 0


    def Test(self, browser, client):
        if(self.wait()):
            url = browser.current_url
            if(str(url) != '' and ("/hledej?" not in str(url))):
                url = url.split("#!")[0]
                if(url.startswith("https://ulozto.cz/file/") or url.startswith("https://uloz.to/file/")):
                    client.publish("house/ulozto",url)
                    print("URL saved, searching for next.")
                else:
                    print("Wrong URL")
                    self.Test(browser, client)
            else:
                print("Wrong URL")
                self.Test(browser, client)
        else:
            print("OK, skipping, searching for next.") 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MyApp()
    gui.show()
    sys.exit(app.exec_())

    
