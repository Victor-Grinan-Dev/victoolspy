import requests

one_call_weather = 'https://api.openweathermap.org/data/2.5/onecall'
appid = '80e877059407012cbef59f8ac82bcf1c'

PART = 'current,minutely,daily'
helsinki = {'lat': 60.169857, 'lon': 24.938379}

lat = helsinki['lat']
lon = helsinki['lon']

params = {
    'lat': lat,
    'lon': lon,
    'exclude': PART,
    'appid': appid
}

response = requests.request(method='GET', url=one_call_weather, params=params)
data = response.json()['hourly'][:12]
is_rainy = False

for hour_data in data:
    weather = hour_data['weather'][0]['id']
    if weather < 700:
        is_rainy = True

if is_rainy:
    print('Bring an umbrela')
