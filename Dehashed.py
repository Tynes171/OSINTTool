import requests
import json
from pprint import *

with open('auth.json') as json_file:
	data = json.load(json_file)

API_KEY = data['dehashedkey']
user = data['dehasheduser']


def retrieve_hits(username = 'justin'):

    global API_KEY
    global user

    url = 'https://api.dehashed.com/search'
    auth = (user, API_KEY)
    headers = {'Accept': 'application/json'}
    params = {'query': username}

    try:
        res = requests.get(url, auth = auth, headers = headers, params = params)
        print(res.raise_for_status())
    except Exception as e:
        return "Failed Becuase of a {}".format(e)
    
    originalData = res.json()
    data = json.dumps(res.json(), sort_keys = True, indent = 2)
    

    answer = ''

    i = 0
    while i < len(originalData['entries']) and i <= 4:

        answer += "------- RESULT {} --------".format(i)
        answer += "{} ".format(json.dumps(originalData['entries'][i], sort_keys = True, indent = 2))


        i = i + 1 

    print(answer)
    return answer
    

    '''
    originalData = res.json()
    data = json.dumps(res.json(), sort_keys = True, indent = 2)
    "{} ".format(json.dumps(originalData['entries'][i], sort_keys = True, indent = 2))
    
    
    '''