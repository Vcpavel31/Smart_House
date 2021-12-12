import json
import mysql.connector 

from datetime import datetime, timedelta
from urllib import request, parse

def Read_KEY():
    with open('../auth.key', 'r') as j:
         contents = json.loads(j.read())
    return contents

def Get_ID(data):
    ID = str(data)
    disallowed_characters = """[]{}""'' """
    for character in disallowed_characters:
        ID = ID.replace(character, "")
    return int(ID.split(",")[0])

test_SQL = "SELECT CURRENT_TIMESTAMP;"
    
data = Read_KEY()
ID = Get_ID(data['Used_ID'])

if(data['Used_type'] == ['MariaDB']):
    print("Direct connection to MariaDB")
    connection = data['MariaDB'][ID]
    
    mydb = mysql.connector.connect(
          host=connection['Adress'],
          port=connection['Port'],
          user=connection['Username'],
          password=connection['Password'],
          database=connection['Database']
    )

    if(mydb.cursor() != ""):
        print("Connected")
        mycursor = mydb.cursor()
        mycursor.execute(test_SQL)
        system_time = datetime.now()
        DB_time = mycursor.fetchall()[0][0]
        if(system_time + timedelta(0,1) > DB_time and system_time -  + timedelta(0,1) < DB_time):
            print("Selected MariaDB connection is working.")
        else:
            print("Selected MariaDB server has different time.")
    else:
        print("Selected MariaDB failed to connect.")
        raise ValueError("Not Connected")

else:
    if(data['Used_type'] == ['WWW_unsecure']):
        print("Connection to MariaDB through unsecure web")
        connection = data['WWW_unsecure'][ID]
        data = {"MYSQL": test_SQL}
        req =  request.Request(connection['Adress'], data=json.dumps(data).encode('utf-8'))
        resp = request.urlopen(req)
        print(resp.read())
        
    else:
        print("Unkown or undefined used connection type")
