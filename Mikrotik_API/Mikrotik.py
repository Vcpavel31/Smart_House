#!/usr/bin/python
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta
import sys
import os
import time
import json

import mysql.connector

import routeros_api

def get_cpu_temperature():
    tFile = open('/sys/class/thermal/thermal_zone0/temp')
    temp = float(float(tFile.read())/1000)
    return temp

json_string = """
{
    "sensors": {
        "cpu": [
            {
                "sensor": "11"
            }
        ],
        "cpu-temperature": [
            {
                "sensor": "387"
            }
        ],
        "power-consumption": [
            {
                "sensor": "388"
            }
        ],
        "psu1-voltage": [
            {
                "sensor": "389"
            }
        ],
        "psu2-voltage": [
            {
                "sensor": "390"
            }
        ],
        "psu1-current": [
            {
                "sensor": "391"
            }
        ],
        "psu2-current": [
            {
                "sensor": "392"
            }
        ]
    }
}
"""

connection = routeros_api.RouterOsApiPool(
    "10.0.0.18",
    username='xxx',
    password='xxxxxx',
    port=8728,
    plaintext_login=True
)

api = connection.get_api()
list_system_health = api.get_resource('/system/health')
response = json.loads(json.dumps(list_system_health.get()))
data = json.loads(json_string)
for x in response[0]:
    data["sensors"][x][0]["value"]=response[0][x]
    
data["sensors"]["cpu"][0]["value"]=get_cpu_temperature()
            
try:
    print("Connecting")
    mydb = mysql.connector.connect(
      host="10.0.0.16",
      user="xxx",
      password="xxxxxx",
      database="xxxxxxxxx"
    )
    mycursor = mydb.cursor()
    if(mycursor != ""):
        print("Connected")
        
        for x in data["sensors"]:
            try:
                sql = "INSERT INTO `Values`(`Sensor`, `Time`, `Hodnota`) VALUES ('"+str(data["sensors"][x][0]["sensor"])+"', CURRENT_TIMESTAMP, '"+str(data["sensors"][x][0]["value"])+"')"
                print("'"+str(sql)+"'")
                mycursor.execute(sql)    
            except Exception as e:
                pass

        f = open("/home/pi/NODB.txt", "r+")
        for data in f.read().split("&"):
            if(str(data) != ""):
                try:
                    for x in data["sensors"]:
                        try:
                            sql = "INSERT INTO `Values`(`Sensor`, `Time`, `Hodnota`) VALUES ('"+str(data["sensors"][x][0]["sensor"])+"', '"+str(data["Time"])+"', '"+str(data["sensors"][x][0]["value"])+"')"
                            print("'"+str(sql)+"'")
                            mycursor.execute(sql)    
                        except Exception as e:
                            pass
                except:
                    error_file = open("/home/pi/NODB_ER.txt", "a")
                    error_file.write(data+"!")
                    error_file.close()

        mydb.commit()
        f.truncate(0)
        f.close()
        mydb.close()
    else:
        raise Exception("Something went wrong with sending data.")

except Exception as e:
    print (e)
    f = open("/home/pi/NODB.txt", "a")
    data["Time"]=str(datetime.now()+timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    f.write(str(data)+"&")
    f.close()
    exit()   


print (datetime.now()+timedelta(hours=1))
