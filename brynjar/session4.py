# -*- coding: utf-8 -*-
import requests
from dateutil import parser
with open("../secret") as secret:
    password = secret.read().strip()
AUTH = ("binnisb",password)
COMMITS_URL =  "https://api.github.com/repos/pythonkurs/{0}/commits"
REPOS_URL = "https://api.github.com/orgs/pythonkurs/repos"

    
users = requests.get(REPOS_URL, auth=AUTH)
users_data = users.json()
print len(users_data)
users_name = [user["name"] for user in users_data]

commit_histories = []
for user in users_name:
    print user
    commit_response = requests.get(COMMITS_URL.format(user),auth=AUTH)
    
    commits = commit_response.json()
    print commits
    for d in commits:
        c = [d["commit"]["message"], parser.parse(d["commit"]["author"]["date"])]
        commit_histories.append(c)
        print c
print len(commit_histories)
