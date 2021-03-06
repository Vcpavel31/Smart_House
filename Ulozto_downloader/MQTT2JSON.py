import os
import json
import paho.mqtt.client as mqtt
import time

broker_address="10.0.0.16"
port=1883
data = {}
data['Download'] = []
data['Downloading'] = []
data['Downloaded'] = []

try:
    data = json.loads(str(open('mem.json', 'r').read()))
except:
    f = open('mem.json', 'w')
    json.dump(data, f)
    f.close()
    
def on_message(client, userdata, message):
    data = json.loads(str(open('mem.json', 'r').read()))
    data['Download'].append(str(message.payload.decode("utf-8")))
    print(message.payload.decode("utf-8"))
    myFile = open("mem.lock", "w+")
    myFile.close()
    f = open('mem.json', 'w')
    json.dump(data, f)
    f.close()
    os.remove("mem.lock")

def connect(client):
    try:
        client.connect(broker_address,port) #connect to broker
        print("Connected to MQTT broker")
        while(1):
            client.loop_start() #start the loop
            print("Subscribing to topic","house/ulozto")
            client.subscribe("house/ulozto")
            time.sleep(3595)
            client.loop_stop()
    except:
        print("Connection failed trying again in 30 seconds.")
        time.sleep(30)
        connect(client)

def start():
    data = json.loads(str(open('mem.json', 'r').read()))
    sort = {}
    sort['Download'] = []
    sort['Downloading'] = []
    sort['Downloaded'] = data["Downloaded"]
    for url in data["Download"]:
        if(url not in data["Downloaded"]):
            if(url not in sort['Download']):
                sort['Download'].append(url)
    for url in data["Downloading"]:
        if(url not in data["Downloaded"]):
            if(url not in sort['Download']):
                sort['Download'].append(url)
    
    f = open('mem.json', 'w')
    json.dump(sort, f)
    f.close()
    print("Deduplication done!")

start()

print("creating new instance")
client = mqtt.Client("Downloader_2") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
connect(client)


