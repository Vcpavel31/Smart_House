import json

data_to_add={
    'Adress': '10.0.0.16',
    'Port': '3308',
    'Username': 'TEST',
    'Password': '123456789',
    'Database': 'Test_DB',
}
target_connection = 'MariaDB'

def Read_KEY():
    with open('../auth.key', 'r') as j:
         contents = json.loads(j.read())
         print(contents)
    return contents

data = Read_KEY()

if(data_to_add not in data[target_connection]):
    print("Adding new entry to: ", target_connection, "with value:", data_to_add)
    data[target_connection].append(data_to_add)
    with open('../auth.key', 'w') as outfile:
        json.dump(data, outfile)
else:
    print("Data already in file!")
