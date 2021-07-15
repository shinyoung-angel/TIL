import requests
from bs4 import BeautifulSoup 

# response = requests.get('http://naver.com')
response = requests.get('http://naver.com').text

print(response)