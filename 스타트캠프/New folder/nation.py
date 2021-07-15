import requests


name='Bob'
url=f'https://nationalize.io/?name={name}'
response=requests.get(url).json()

print(response)

name=response['name']
country_id=response['country'][0]['country_id']
country_probability=response['country'][0]['country_id']