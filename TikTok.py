import requests
import bs4
import json



res = requests.get('https://www.tiktok.com/@shekaahm')
res.raise_for_status()
print(res.text)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

urls = soup.select('div .jsx-1410658769')

print(urls[:20])






