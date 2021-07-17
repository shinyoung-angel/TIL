import requests

key ='jG7D8D72zopRRUhXtnCJSYUudM%2B4fBQ8zmG%2BlrICYPzKdRfeuC6IevVrx8vOtEFviQ9RH0RcznoaMMm76gbC0w%3D%3D'
local='부산'
url=f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?servicekey={key}&sidoName={local}&returnType=json'
print(url)

#부산의 미세먼지 농도는 ---입니다.

response=requests.get(url).json()
value=response['response']['body']['items'][1]['stationName']
value2=response['response']['body']['items'][1]['pm10Value']
print(value)
print('부산 %s의 미세먼지 농도는 %d입니다.'%(value,int(value2)))