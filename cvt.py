import json
f = open("heat_data.json", 'r')
w = open("heat_data_parsed_json", 'w')
#print(f.read())
j = json.loads(f.read())
#print(len(j))
data = "["
for i in j:
    data += "[%s, %s]," % ( i['lat'], i['lng'])
data += "]"
print(data)
