from scripts.get_repo import *
import json
from json import *
print("----")
with open("config/config.json") as json_file:
        json_data = json.load(json_file)     
print("[*] Getting Repositories of: " + str(json_data["user"]))
print("----")
get_repo()

