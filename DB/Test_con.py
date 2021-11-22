import json
import mysql.connector 

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
    
data = Read_KEY()
ID = Get_ID(data['Used_ID'])

if(data['Used_type'] == ['MariaDB']):
    print("Direct connection to MariaDB")
    connection = data['MariaDB'][ID]
    mydb = mysql.connector.connect(
          host=str(connection['Adress']).replace("'", ""),
          port=str(connection['Port']).replace("'", ""),
          user=str(connection['Username']).replace("'", ""),
          password=str(connection['Password']).replace("'", ""),
          database=str(connection['Database']).replace("'", "")
    )

    if(mydb.cursor() != ""):
        print("Connected")
        print("Selected MariaDB connection is working.")
    else:
        print("Selected MariaDB failed to connect.")
        raise ValueError("Not Connected")

else:
    print("Unkown or undefined used connection type")
