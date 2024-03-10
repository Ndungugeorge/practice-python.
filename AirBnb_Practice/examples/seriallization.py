import json

"""converting dictionary to json file"""
data ={
    "name": "George",
    "age": 21,
    "course": "IT",
    "units": ["Alx","DSS","Data mining","SQA"]
}

info_json = json.dumps(data,indent=4)
with open("serializ.json",'a') as file:
    file.write(info_json + '\n')