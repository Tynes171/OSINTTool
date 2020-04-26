import twint
import os
import sqlite3
import sys


import Instagram





def profile_extraction(username = "Somebody"):

	c = twint.Config()
	c.Hide_output = True
	c.Username = username
	c.Output = username+".txt"
	twint.run.Lookup(c)

	if not os.path.exists(username+'.txt'):
		f = open(username+'.txt', 'w')
		f.close()

	try:
		with open(username+'.txt', 'r', encoding = 'utf-8') as f:
			profile = f.read().replace('|', '\n')

		os.remove(username+'.txt')

		return profile
	except Exception as e:
		return "No Results because of {}".format(e)

def birthday_extraction(username = "Somebody"):

	#c.Username = username
	c = twint.Config()
	c.Hide_output = True	
	c.Database = username+".db"
	c.To = username
	
	c.Search = "Happy Birthday"
	response = ''
	twint.run.Search(c)

	try: 
		conn = sqlite3.connect(username+'.db')
		curs = conn.cursor()
		curs.execute('''SELECT COUNT(date) AS hits, date as birthday FROM tweets GROUP BY date''')
		rows = curs.fetchall()
		for row in rows:
			#print(row)
			response = "{} {} {}\n".format(response, row[0], row[1]) 

		conn.close()
		#print("Response\n {}".format(response))
 

		#
		
	except Exception as e:
		return "No Results because of {}".format(e)

	'''
	finally:
		os.remove(username+'.db')
	'''
	return response


def general_extraction(username = "Somebody", query = "H", limit = 10):
	c = twint.Config()
	#c.Hide_output = True
	c.Username = username
	c.Search = query
	
	
	c.Limit = limit
	sys.stdout = open('temp.txt', 'w', encoding = 'unicode-escape')
	twint.run.Search(c)
	sys.stdout.close()
	response = ''
	temp = open('temp.txt', 'rb')

	lines = temp.readlines()

	for line in lines:
		response += str(line, 'unicode-escape')
	
	temp.close()
	os.remove('temp.txt')

	return response
	





	
if __name__ == '__main__':
	username = 'justin'
	#print(profile_extraction(username))
	#print(birthday_extraction(username))
	print(general_extraction(username))