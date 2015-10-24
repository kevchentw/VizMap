import json
f = open("heat_data2.json", 'r')
#print(f.read())
j = json.loads(f.read())
#print(len(j))
data = "["
for i in j:
    data += "[%s, %s]," % ( i['lat'], i['lng'])
data += "]"
print(data)
