import requests
import json


def breached_accounts(email):
	API_KEY = '902ec87b3eb54bd5a4f34b00e9da4e3f'


	url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'

	header = {'hibp-api-key': API_KEY }
	try:
		res = requests.get(url + email, headers = header)
		print(res.raise_for_status())

		data = res.json()

		return data
	except Exception as e:
		return "Failed due to {}".format(e)
