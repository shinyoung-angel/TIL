import requests

key ='jG7D8D72zopRRUhXtnCJSYUudM%2B4fBQ8zmG%2BlrICYPzKdRfeuC6IevVrx8vOtEFviQ9RH0RcznoaMMm76gbC0w%3D%3D'
local='부산'
url=f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?servicekey={key}&sidoName={local}&returnType=json'


response=requests.get(url).json()
value2=response['response']['body']['items'][1]['pm10Value']

TOKEN='1778099467:AAGfAKdXhw4iVcFbkpMB44A1FYK1Kgpl2B8'
url=f'https://api.telegram.org/bot{TOKEN}'
update_url=f'{url}/getUpdates'
b=requests.get(update_url).json()
a=b['result'][0]['message']['chat']['id']

