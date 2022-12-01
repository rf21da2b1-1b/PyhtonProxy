import requests

URL = 'http://127.0.0.1:5191/api/Biler/'

def GetAll():
    response = requests.get(URL)
    data = response.json()
    return data, response


def GetOne(stelNummer):
    response = requests.get(URL+stelNummer)
    data = response.json()
    return data, response


def Add(bil):
    response = requests.post(URL, json=bil)
    return response


def Delete(stelNummer):
    response = requests.delete(URL+stelNummer)
    return response


def Edit(bil):
    updateUrl = URL + bil['stelNummer']
    response = requests.put(updateUrl, json=bil)
    return response
