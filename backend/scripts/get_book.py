import requests 
import re 
from bs4 import BeautifulSoup


search_term = 'catcher in the rye'

search_term = re.sub('\s','+',search_term)

SEARCH_URL = 'https://libgen.gs/index.php?req={}&columns%5B%5D=t&columns%5B%5D=a&columns%5B%5D=s&columns%5B%5D=y&columns%5B%5D=p&columns%5B%5D=i&objects%5B%5D=f&objects%5B%5D=e&objects%5B%5D=s&objects%5B%5D=a&objects%5B%5D=p&objects%5B%5D=w&topics%5B%5D=l&topics%5B%5D=c&topics%5B%5D=f&topics%5B%5D=a&topics%5B%5D=m&topics%5B%5D=r&topics%5B%5D=s&res=25&filesuns=all'.format(search_term)

input_url = requests.get(SEARCH_URL)

soup = BeautifulSoup(input_url.text,'lxml')

