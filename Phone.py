'''

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'XB65bee4ad5be08e28368def1be1a3efee'
auth_token = 'a138c4646fd34230ab9fa7673c3bfe36'
client = Client(account_sid, auth_token)
number = input("Enter a phone Number to search\n")
phone_number = client.lookups.phone_numbers(number).fetch(country_code='US', add_ons=['ekata_reverse_phone'])

print(phone_number.add_ons)
'''


import requests, json

'''
ag = argparse.ArgumentParser()

ag.add_argument("-p","--phonenumber", default="2404681335", help="Phone Number to look up")

ap = ag.parse_args()

number = ap.phonenumber
'''


account_sid = 'AC4d781cfc8b5615429058ce10e2f1499f'
auth_token = 'a138c4646fd34230ab9fa7673c3bfe36'

params = {'AddOns': 'ekata_reverse_phone'}



def get_addresses(num = '3018081224'):



	url = 'https://lookups.twilio.com/v1/PhoneNumbers/+1'+num


	req = requests.get(url, params, auth=(account_sid, auth_token))
	req.raise_for_status()
	res = req.json()#json.loads(req.text)
	data = json.dumps(res, indent=2, sort_keys=True)
	print(res)


	with open(num+'.json', 'w') as f:
	   	f.write(data)

	#print(res)
	# input()


	answer = ''
	try:

		firstname = res['add_ons']["results"]["ekata_reverse_phone"]["result"]["belongs_to"]["firstname"]
		lastname = res['add_ons']["results"]["ekata_reverse_phone"]["result"]["belongs_to"]["lastname"]
		gender = res['add_ons']["results"]["ekata_reverse_phone"]["result"]["belongs_to"]["gender"]
		associatedPeople = res['add_ons']["results"]["ekata_reverse_phone"]["result"]["associated_people"]

	except Exception as e:
		print(e)
		return 'No Results'
		
	results = res['add_ons']["results"]["ekata_reverse_phone"]["result"]["current_addresses"][0]
	if firstname != None:
		answer += "Firstname: {}\n".format(firstname)
	
	if lastname != None:
		answer += "Lastname: {}\n".format(lastname)
	
	if gender != None:
		answer += "Gender: {}\n".format(gender)
		
	if results['street_line_1'] != None:	
		answer += "Address: {}\n".format(results['street_line_1'])
	
	if results['street_line_2'] != None:
		answer += "{}\n".format(results['street_line_2'])
		
	if results['city'] != None:
		answer += "City: {}\n".format(results['city'])
		
	if results['postal_code'] != None:	
		answer += "Zip Code: {}\n".format(results['postal_code'])
	
	if results['state_code'] != None:
		answer += "State: {}\n".format(results['state_code'])
	
	if associatedPeople != None:
		answer += "Associated People: \n"
		for person in associatedPeople[:5]:
			answer += "Person: {}\nRelation: {}\n".format(person["name"], person["relation"])



	return answer








