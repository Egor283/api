import requests

def get_cord(address):
    server = 'http://geocode-maps.yandex.ru/v1/?'
    geocode = f'{server}apikey=8013b162-6b42-4997-9691-77b7074026e0&geocode={address}&format=json'
    res = requests.get(geocode)
    if res:
        j = res.json()
        r = j['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        coord = r['Point']['pos']
        x, y = coord.split()
        return float(x), float(y)
    return f'Http статус:", {res.status_code}, "(", {res.reason}, ")'


def get_ll_span(address):
    server_address = 'http://geocode-maps.yandex.ru/v1/?'
    api_key = '8013b162-6b42-4997-9691-77b7074026e0'
    geocoder_request = f'{server_address}apikey={api_key}&geocode={address}&format=json'

    response = requests.get(geocoder_request)
    if response:
        response_json = response.json()
        toponym = response_json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    if not toponym:
        return (None, None)

    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    ll = ",".join([toponym_longitude, toponym_lattitude])

    envelope = toponym["boundedBy"]["Envelope"]

    l, b = envelope["lowerCorner"].split(" ")
    r, t = envelope["upperCorner"].split(" ")

    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0

    span = f"{dx},{dy}"

    return ll, span