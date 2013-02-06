# -*- coding: utf-8 -*-
import operator
def get_commits_for_pythonkurs(limit=100000):
    import requests
    from dateutil import parser
    from pandas import DataFrame,Series
    with open("/home/binni/MasterProject/scilifelabpython/Brynjar/secret") as secret:
        password = secret.read().strip()
    AUTH = ("binnisb",password)
    COMMITS_URL =  "https://api.github.com/repos/pythonkurs/{0}/commits"
    REPOS_URL = "https://api.github.com/orgs/pythonkurs/repos"
    
    users = requests.get(REPOS_URL, auth=AUTH)
    users_data = users.json()
    users_name = [user["name"] for user in users_data]
    commit_histories = {}
    for user in users_name[:limit]:
        commit_response = requests.get(COMMITS_URL.format(user),auth=AUTH)
        commits = commit_response.json()
        ser = []
        ind = []
        for d in commits:
            ser.append(d["commit"]["message"])
            ind.append(parser.parse(d["commit"]["author"]["date"]))
        commit_histories[user] = Series(data=ser,index=ind,name=user,dtype=str)
    df = DataFrame(commit_histories)
    return df

def get_most_common_day_and_hour(df):
    day = _group_by_key(lambda x: x.strftime("%A"),df)
    hour = _group_by_key(lambda x: x.hour,df)
    return (day,hour)

def _group_by_key(lamda_func,df):
    groupped = df.groupby(lamda_func)
    return max(groupped.groups.iterkeys(),key=(lambda k: len(groupped.groups[k])))

if __name__=="__main__":
    df = get_commits_for_pythonkurs()
    (day,hour) = get_most_common_day_and_hour(df)
    print day,hour