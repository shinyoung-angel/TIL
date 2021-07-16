import requests

location=1132599
url=f'https://www.metaweather.com/api/location/{location}/'
response=requests.get(url).json()

weather_state_name=response['consolidated_weather'][2]['weather_state_name']
applicable_date=response['consolidated_weather'][2]['applicable_date']
print(weather_state_name)
print(applicable_date)