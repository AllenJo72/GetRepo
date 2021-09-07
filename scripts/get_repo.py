from github import Github
from json import *
import json
_gitH = Github()

def get_repo():
    with open("config/config.json") as json_file:
        json_data = json.load(json_file)
    ps = str(json_data["user"])
    user = _gitH.get_user(ps)
    repos = user.get_repos()
    non_forks = []
    for repo in user.get_repos():
        if repo.fork is False:
            non_forks.append(repo.name)
    print(str(non_forks))        
    ps1 = str(json_data["save"])
    if ps1 =="True":       
        m = '"'
        filename = "saves/"+ps+".txt"
        write_file = open(filename, 'w')
        non_forks = map(lambda x:x+'\n', non_forks)
        write_file.writelines(non_forks)
        write_file.close()
        print("Saved in /saves")
    else:
        print("Did not save the output to any file, if it was needed change the save value in the config file to 'True'")            
