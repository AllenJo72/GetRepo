from json import *
import json


with open("GetRepo/config/config.json") as json_file:
        json_data = json.load(json_file)
#ps = print(json_data["name"])

if json_data["user"] == "AllenJo72":
    print("Meh") 
else:
    print("Bleh")