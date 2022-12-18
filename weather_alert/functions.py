import requests

one_call_weather = 'https://api.openweathermap.org/data/2.5/onecall'
appid = '80e877059407012cbef59f8ac82bcf1c'

PART = 'hourly', 'daily'
helsinki = {'lat': 60.169857, 'lon': 24.938379}
miami = {'lat': 25.761681, 'lon': -80.191788}
havana = {'lat': 37.091736, 'lon': -95.941925}


def farenheit_to_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    return celcius


def kelvis_to_celcious(kelvins):
    celcius = kelvins - 273.15
    return celcius


def set_city(cityname):
    lat_ = cityname['lat']
    lon_ = cityname['lon']
    return lat_, lon_


def set_params(cityname):
    lat, lon = set_city(cityname)

    params = {
        'lat': lat,
        'lon': lon,
        'exclude': PART,
        'appid': appid
    }
    return params


def weather(cityname):
    params = set_params(cityname)
    response = requests.request(method='GET', url=one_call_weather, params=params)
    return response.json()


if __name__ == '__main__':

    # print(set_city(miami))
    # print(set_city(havana))
    # print(set_city(helsinki))

    # print(set_params(miami))
    # print(set_params(havana))
    # print(set_params(helsinki))

    temp_k = weather(miami)['current']['temp']
    temp_c = kelvis_to_celcious(temp_k)
    print(temp_c)
    temp_k = weather(havana)['current']['temp']
    temp_c = kelvis_to_celcious(temp_k)
    print(temp_c)
    temp_k = weather(helsinki)['current']['temp']
    temp_c = kelvis_to_celcious(temp_k)
    print(temp_c)