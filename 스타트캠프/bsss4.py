import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
data=BeautifulSoup(response, 'html.parser')
kospi=data.select_one('#KPI200_now')
result=kospi.text
print(f'{result}입니다 이자슥')

