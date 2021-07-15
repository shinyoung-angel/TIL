import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
data=BeautifulSoup(response, 'html.parser')
kospi=data.select_one('#container > div.market_include > div > div.market1 > div.title > h2')
result=kospi.text
print(f'{result}입니다 이자슥')

