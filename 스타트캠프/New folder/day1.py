import requests
from bs4 import BeautifulSoup

url='https://alphasquare.co.kr/home/market/market-summary?code=005935   '
response=requests.get(url).text
data=BeautifulSoup(response, 'html.parser')
summary=data.select_one('#stock-005935 > div.stock-contents.alive-stock > div.lower-content.price-color > h3')
result=summary.text
print(f'{result}이거다 이놈앙')