import twint
import os
import sqlite3
import sys





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
		curs.execute('''SELECT COUNT(date) as hits, date as birthday FROM tweets GROUP BY date''')
		rows = curs.fetchall()
		for row in rows:
			#print(row)
			response = "{} {} {}\n".format(response, row[0], row[1]) 


		#print("Response\n {}".format(response))

		
	except Exception as e:
		print(e)

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
	sys.stdout = open('temp.txt', 'w')
	twint.run.Search(c)
	sys.stdout.close()
	response = ''
	with open('temp.txt', 'r') as temp:
		response += temp.read()
	
	os.remove('temp.txt')

	return response
	'''
	try:
		 
		conn = sqlite3.connect(username+'.db')
		curs = conn.cursor()
		curs.execute(SELECT date, time, timezone, tweet, screen_name FROM tweets )
		rows = curs.fetchall()
		for row in rows:
			#print(row)
			response += "{} {} {} {}\n".format(row[0], row[1], row[2], row[3]) 
		os.remove(username+'.db')
		return response

	except Exception as e:
		print(e)
		return "No Results"
	'''
	






	
if __name__ == '__main__':

	print(profile_extraction("icantstophim"))
	print(birthday_extraction("icantstophim"))
	print(general_extraction("icantstophim"))