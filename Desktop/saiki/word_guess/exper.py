import json
with open('data.json', 'r') as fp:
    data = json.load(fp)

for i in data.keys() :
    if(len(data[i]) >5 ) :
        print (i, data[i])
