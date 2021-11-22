import json

data = {}
data['Used_type'] = []
data['Used_ID'] = []
data['MariaDB'] = []

with open('../auth.key', 'w') as outfile:
    json.dump(data, outfile)
