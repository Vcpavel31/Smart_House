import os
import json
import time
import subprocess
import shutil
import sys

global url_global
url_global = ""
global Done
Done = ""

def ERROR(url):
    if(url != ""):
        print("ulozto-downloader  --auto-captcha --parts 100 --output /home/pi/downloader/ "+str(url))
        if(os.path.isfile("mem.lock")):
            time.sleep(45)
            ERROR(url)
        else:
            myFile = open("mem.lock", "w+")
            myFile.close()
            data = json.loads(str(open('mem.json', 'r').read()))
            data["Download"].append(url)
            f = open('mem.json', 'w')
            json.dump(data, f)
            f.close()
            os.remove("mem.lock")
        return 1
    return 0

def check_LOCK():
    if(os.path.isfile("mem.lock")):
        time.sleep(45)
        check_LOCK()
    else:
        myFile = open("mem.lock", "w+")
        myFile.close()
        data = json.loads(str(open('mem.json', 'r').read()))
        print("Amount of URLs to download: "+str(len(data["Download"])))
        global url_global
        url_global = (data["Download"][0])
        del data["Download"][0]
        data["Downloading"].append(url_global)
        f = open('mem.json', 'w')
        json.dump(data, f)
        f.close()
        os.remove("mem.lock")
        #process = subprocess.Popen("lxterminal --title=Downloader --command='ulozto-downloader  --auto-captcha --parts 53 --output /home/pi/downloader/ "+str(url)+"'", shell=True, stdout=subprocess.PIPE)
        print("Starting download of: "+str(url_global))
        process = subprocess.run("ulozto-downloader  --auto-captcha --parts 100 --output /home/pi/downloader/ "+str(url_global), shell=True, capture_output=True)
        try:
            print ("Downloading done.")
            output = (process.stdout.decode('utf-8'))
            shutil.move(output.split("Delete file: ")[1].split(".udown")[0], "/home/pi/downloader/done")
            shutil.move(str(output.split("Delete file: ")[1].split(".udown")[0])+str(".ucache"), "/home/pi/downloader/ucache")
            print ("Moving done.")
            global Done
            Done = url_global
        except:
            ERROR(url_global)
    return 1

def main():
    print("Starting automatic Ulozto downloader.")
    while(1):
        if(json.loads(str(open('mem.json', 'r').read()))["Download"] != []):
            check_LOCK()
        else:
            print ("Waiting for new URL for download. ")
        time.sleep(120)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if(Done != url_global):
            print("KeyboardInterrupt - saving URL: "+str(url_global))
            print(ERROR(url_global))
        else:
            print("File already downloaded. Skipping saving to mem file.")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
