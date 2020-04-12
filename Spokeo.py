import requests
import bs4
import sys




firstname = 'Justin'
lastname = 'Williams'
city = ''
pages = 1
state = 'Georgia'


url = 'https://www.spokeo.com'

terms = "/{}-{}".format(firstname, lastname)

if state is not None: 
	terms += "/{}".format(state)

if city is not None:
	terms += "/{}".format(city) 


page_number = 1


req = requests.get(url + terms)#, params = {'loaded':1})

req.raise_for_status()


#print(req.text)


webparser = bs4.BeautifulSoup(req.text, features="lxml")

names = webparser.select('div .edso92o0')
cities = webparser.select('div .css-1pqe2l9')
#links = webparser.select('a .single-column-list-item')

#relatives = webparser.select('div .top-xs')

for i in  range(len(names)):
	print("Name and Age: {}".format(names[i].getText()))
	#print("URLs: {}{}".format(url, links[i].get('href')))
	print("City: {}\n".format(cities[i].getText()))

	
	#print("Relatives: {} \n".format(relatives[i].getText()))

















