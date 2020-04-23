import requests
import bs4
import sys


firstname = 'Justin'
lastname = 'Williams'
city = 'Atlanta'
pages = 1
state = 'GA'


url = 'https://www.zabasearch.com/people'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

terms = "/{}+{}".format(firstname.lower(), lastname.lower())

if state is not None: 
	terms += "/{}".format(state.lower())



params = {
    'middleInitialFilter':'',
    'cityFilter': city, 
    'filterbutton':'Filter',
    'ageFilter':''
}


req = requests.get(url + terms, params = params)#, headers = headers)#, params = {'loaded':1})

req.raise_for_status()


#print(req.text)


webparser = bs4.BeautifulSoup(req.text, features="html.parser")

names = webparser.select('a .result-person-name')
cities = webparser.select('div .result-person-address')
#links = webparser.select('a .single-column-list-item')

#relatives = webparser.select('div .top-xs')

for i in  range(len(names)):
	print("Name and Age: {}".format(names[i].getText()))
	#print("URLs: {}{}".format(url, links[i].get('href')))
	print("City: {}\n".format(cities[i].getText()))

	
	#print("Relatives: {} \n".format(relatives[i].getText()))


