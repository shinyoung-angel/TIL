# import requests
# location=1132599
# url=f'https://www.metaweather.com/api/location/{location}'
# response=requests.get(url).json()

# weather=response.get('consolidated_weather')[0].get('weather_state_name')
# print(weather)

# import requests
# key='jG7D8D72zopRRUhXtnCJSYUudM%2B4fBQ8zmG%2BlrICYPzKdRfeuC6IevVrx8vOtEFviQ9RH0RcznoaMMm76gbC0w%3D%3D'
# name='울산'
# url=f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={name}&returnType=json'
# print(url)
# response=requests.get(url).json()
# coValue=response.get('response').get('body').get('items')[0].get('coValue')
# print(coValue)


import requests
key='jG7D8D72zopRRUhXtnCJSYUudM%2B4fBQ8zmG%2BlrICYPzKdRfeuC6IevVrx8vOtEFviQ9RH0RcznoaMMm76gbC0w%3D%3D'
name='울산'
url=f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={name}&returnType=json'
a=requests.get(url).json()
Nongdo=a.get('response').get('body').get('items')[0].get('coValue')

TOKEN='1778099467:AAGfAKdXhw4iVcFbkpMB44A1FYK1Kgpl2B8'
url_1=f'https://api.telegram.org/bot{TOKEN}'
update_url=f'{url}/getUpdates'
# b=requests.get(update_url).json()

# id=b['result'][0]['message']['chat']['id']
# last=b['result'][-1]['message']['text']

# text='미칭'

# if last=='농도미세':
#     text=f'울산 농도미세 농도농도 {Nongdo}라능'

# message_url=f'{url_1}/sendMessage?id={id}&text={text}'
# requests.get(message_url)


print(update_url)


import os

cwd=os.getcwd()


adf'afdadfad'