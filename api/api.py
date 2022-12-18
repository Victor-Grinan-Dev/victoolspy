import requests

response = None


def call_API(url: str, key=None, params=None):
    global response
    """
    basic steps for a API request
    :param params: all params requested from API
    :param url: recive it already with the needed arguments included
    :param key: if the API call needs a key
    :return: the json data formated 
    """
    if "http://" not in url:
        url = "http://" + url
    if key:
        url = url + f'appid={key}'

        if params:
            response = requests.get(url, params)
    else:
        response = requests.get(url)

    response.raise_for_status()
    data = response.json()
    return data


key = "80e877059407012cbef59f8ac82bcf1c"

vallila_position = 60.1944, 24.9570

endpoint_coor = 'api.openweathermap.org/data/2.5/weather?'
weather_params = {
    'lat': vallila_position[0],
    'long': vallila_position[1],
    'appid': key
}

call_API()
