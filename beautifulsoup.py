from bs4 import BeautifulSoup as bs
import requests
url='http://bing.com'
r=requests.get(url)
tree=bs(r.text, 'html.parser')
for link in tree.findAll('a'):
    print(f'{link.get('href')}-->{link.text}')
