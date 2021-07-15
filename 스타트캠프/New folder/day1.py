import requests
from bs4 import BeautifulSoup

url='https://alphasquare.co.kr/home/stock/stock-summary?code=005930'
response=requests.get(url).text
data=BeautifulSoup(response, 'html.parser')
summary=data.select_one('#main-chart > div.stock-nav > div.stock-nav-stock-info.shortened-info > div > div.name > h2')
result=summary.text
print(f'{result}이거다 이놈앙')