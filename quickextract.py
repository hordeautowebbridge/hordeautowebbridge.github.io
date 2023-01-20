import json

# Opening JSON file
f = open('db.json')

# returns JSON object as
# a dictionary
data = json.load(f)

od = []

# Iterating through the json
# list
for i in data:
    nn = data[i]['name']
    if('config' in data[i]):
        ff = data[i]['config']['download'][0]['file_name']
        od.append({"name":nn,"file":ff})


# Closing file
f.close()

print(od)