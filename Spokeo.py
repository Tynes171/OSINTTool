import requests
import bs4
import sys




firstname = 'Justin'
lastname = 'Williams'
city = 'Atlanta'
pages = 1
state = 'Georgia'


url = 'https://www.spokeo.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

terms = "/{}-{}".format(firstname, lastname)

if state is not None: 
	terms += "/{}".format(state)

if city is not None:
	terms += "/{}".format(city) 


page_number = 1


req = requests.get(url + terms, headers = headers)#, params = {'loaded':1})

req.raise_for_status()


#print(req.text)


webparser = bs4.BeautifulSoup(req.text, features="html.parser")

names = webparser.select('div .edso92o0')
cities = webparser.select('div .eapx82z0')
#links = webparser.select('a .single-column-list-item')

#relatives = webparser.select('div .top-xs')

for i in  range(len(names)):
	print("Name and Age: {}".format(names[i].getText()))
	#print("URLs: {}{}".format(url, links[i].get('href')))
	print("City: {}\n".format(cities[i].getText()))

	
	#print("Relatives: {} \n".format(relatives[i].getText()))

















