import json

with open("serializ.json",'r') as file:
    json_string = file.read()

    data = json.loads(json_string)

print(data["name"])
print(data["age"])
print(data["course"])
print(data["units"])