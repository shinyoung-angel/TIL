import requests


TOKEN='1778099467:AAGfAKdXhw4iVcFbkpMB44A1FYK1Kgpl2B8'

url=f'https://api.telegram.org/bot{TOKEN}'

#응답내용 저장하기
update_url=f'{url}/getUpdates'
b=requests.get(update_url).json()
#chat_id 뽑기
# a=b.get('result')[0].get('message').get('chat').get('id')
a=b['result'][0]['message']['chat']['id']
print(a)

location=1132599
url_weather=f'https://www.metaweather.com/api/location/{location}/'
response=requests.get(url_weather).json()

the_temp=response['consolidated_weather'][2]['the_temp']
applicable_date=response['consolidated_weather'][2]['applicable_date']
print(the_temp)
print(applicable_date)

# text='%s서울의 기온은 %d도입니다'%(str(applicable_date),the_temp)
# message_url=f'{url}/sendMessage?chat_id={a}&text={text}'
# requests.get(message_url)

#----------------------------------------------------------------------------
key ='jG7D8D72zopRRUhXtnCJSYUudM%2B4fBQ8zmG%2BlrICYPzKdRfeuC6IevVrx8vOtEFviQ9RH0RcznoaMMm76gbC0w%3D%3D'
local='부산'
url=f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?servicekey={key}&sidoName={local}&returnType=json'

#부산의 미세먼지 농도는 ---입니다.

dust=requests.get(url).json()
value=dust['response']['body']['items'][1]['stationName']
value2=dust['response']['body']['items'][1]['pm10Value']

text='부산 %s의 미세먼지 농도는 %d입니다.'%(value,int(value2))
message_url=f'{url}/sendMessage?chat_id={a}&text={text}'
requests.get(message_url)