import requests
import json
from pprint import *

def retrieve_hits(username = 'justin'):

    API_KEY = "f3d375646efe3e519a9efdd841189b40"

    url = 'https://api.dehashed.com/search'
    auth = ('smithsapis@gmail.com', API_KEY)
    headers = {'Accept': 'application/json'}
    params = {'query': username}


    res = requests.get(url, auth = auth, headers = headers, params = params)
    print(res.raise_for_status())
    originalData = res.json()
    data = json.dumps(res.json(), sort_keys = True, indent = 2)
    

    answer = ''

    i = 0
    while i < len(originalData['entries']) and i <= 5:

        answer += "------- RESULT {} --------".format(i)
        answer += "{} ".format(json.dumps(originalData['entries'][i], sort_keys = True, indent = 2))


        i = i + 1 

    print(answer)
    return answer
    

