#!/usr/bin/python
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta
import sys
import os
import time
from subprocess import PIPE, Popen

import mh_z19
import mysql.connector

from waveshare_epd import epd2in13bc
import time
from PIL import Image,ImageDraw,ImageFont,ImageOps
import traceback

def get_cpu_temperature():
    tFile = open('/sys/class/thermal/thermal_zone0/temp')
    temp = float(tFile.read())
    tempC = float(temp/1000)
    return tempC

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

print (datetime.now()+timedelta(hours=1))

print ("Reading sensor")
sensor = mh_z19.read_all()
print ("Reading result: ",sensor)
hodnota = sensor['co2']

if (hodnota == 5000):
    epd2in13bc.epdconfig.module_exit()
    exit()
    raise Exception("Measuring Error")
    
try:
    epd = epd2in13bc.EPD()
    epd.init()
    epd.Clear()
    time.sleep(1)
      
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image  
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)
    
    w, h = drawblack.textsize(str(hodnota)+" ppm", font = font20)
    
    drawblack.text(((epd.width*2-w)/2,  (epd.height/2-h)/2), str(hodnota)+" ppm", font = font20, fill = 0)
    if(hodnota >= 1000):
        drawry.text(((epd.width*2-w)/2, (epd.height/2-h)/2), str(hodnota)+" ppm", font = font20, fill = 0)
    else:
        drawry.rectangle((0, 0, 298, 126), fill = 0)
        
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(ImageOps.invert(HRYimage.convert("RGB"))))
    time.sleep(2)
    epd.sleep()

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
    
        sql = "INSERT INTO `Values`(`Sensor`, `Time`, `Hodnota`) VALUES ('136', CURRENT_TIMESTAMP, '"+str(sensor['co2'])+"')"
        mycursor.execute(sql)
        sql = "INSERT INTO `Values`(`Sensor`, `Time`, `Hodnota`) VALUES ('137', CURRENT_TIMESTAMP, '"+str(sensor['temperature'])+"')"
        mycursor.execute(sql)
        sql = "INSERT INTO `Values`(`Sensor`, `Time`, `Hodnota`) VALUES ('138', CURRENT_TIMESTAMP, '"+str(get_cpu_temperature())+"')"
        mycursor.execute(sql)

        f = open("/home/pi/NODB.txt", "r+")
        for mereni in f.read().split("&"):
            if("|" in mereni):
                try:
                    print (mereni)
                    elements = mereni.split("|")
                    sql = "INSERT INTO `Values`(`Sensor`, `Time`, `Hodnota`) VALUES ('136', '"+str(elements[3])+"', '"+str(float(elements[0]))+"')"
                    print (sql)
                    mycursor.execute(sql)
                    sql = "INSERT INTO `Values`(`Sensor`, `Time`, `Hodnota`) VALUES ('137', '"+str(elements[3])+"', '"+str(elements[1])+"')"
                    print (sql)
                    mycursor.execute(sql)
                    sql = "INSERT INTO `Values`(`Sensor`, `Time`, `Hodnota`) VALUES ('138', '"+str(elements[3])+"', '"+str(elements[2])+"')"
                    print (sql)
                    mycursor.execute(sql)
                except:
                    error_file = open("/home/pi/NODB_ER.txt", "a")
                    error_file.write(mereni+"!")
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
    f.write(str(sensor['co2'])+"|"+str(sensor['temperature'])+"|"+str(get_cpu_temperature())+"|"+(datetime.now()+timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')+"&")
    f.close()
    epd2in13bc.epdconfig.module_exit()
    exit()   
    
print (datetime.now()+timedelta(hours=1))
