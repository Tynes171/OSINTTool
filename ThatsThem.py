import requests
import bs4
import sys






url = 'https://thatsthem.com'

def get_results(firstname, lastname, city, state):

	terms = ''
	terms += r'/name/{}-{}'.format(firstname, lastname)

	if city is not None:
		
		terms += r"/{}".format(city)

	if state is not None:
		terms += r"-{}".format(state)

	print(url + terms)
	#input()
	req = requests.get(url + terms, params = {'loaded':1})

	req.raise_for_status()


	#print(req.text)


	webparser = bs4.BeautifulSoup(req.text, 'html.parser')

	names = webparser.select('div .ThatsThem-record-overview span[itemprop="name"]')
	address = webparser.select('div .ThatsThem-record-address')
	info = webparser.select('dl .row')#'span[itemprop="telephone"]')
	phoneNumbers = webparser.select('span[itemprop="telephone"]')
	email = webparser.select('span[itemprop="email"]')


	i = 0
	j = 0
	text = ''
	try:
		while i <= len(names) and i <= 5:
			

			text += "\n------Entry #{}-----".format(i + 1)
			text += "\nName: {}".format(names[i].getText().strip())
			text += "\nAddress: {}".format(address[i].getText().strip())
			#print("Email: {}".format(email[i].getText().strip()))
			
			i = i + 1

	except IndexError:
		text += 'RESULTS STOP HERE'
		


	finally:
		return text
	#print("Info: {}".format(info[i].getText().strip()))


if __name__ == '__main__':
	get_results('Justin', 'Williams', 'Upper Marlboro', 'MD')

















