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
    
def on_message(client, userdata, message):
    #print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
    data['Download'].append(str(message.payload.decode("utf-8")))
    print(data)
    myFile = open("mem.lock", "w+")
    myFile.close()
    f = open('mem.json', 'w')
    json.dump(data, f)
    f.close()
    import os
    if os.path.exists("mem.lock"):
        os.remove("mem.lock")
    else:
        print("mem.lock")

print("creating new instance")
client = mqtt.Client("Downloader_2") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address,port) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/ulozto")
client.subscribe("house/ulozto")
time.sleep(3595)
client.loop_stop() #stop the loop

