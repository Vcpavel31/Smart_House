import json

data = {}
data['Used_type'] = []
data['Used_ID'] = []
data['MariaDB'] = []
data['WWW_unsecure'] = []

data['MariaDB'].append({
    'Adress': '10.0.0.16',
    'Port': '3308',
    'Username': 'TEST',
    'Password': '123456789',
    'Database': 'Test_DB',
})

with open('../auth.key', 'w') as outfile:
    json.dump(data, outfile)
