from socket import *
import threading
import RestClient
import json


RECEIVER_TO_PORT = 12345
BUFFER_SIZE = 1024


def do_client(buf):
    encoding = 'utf-8'
    fromPi = str(buf, encoding)
    #print(fromPi)
    dict = json.loads(fromPi)
    #print(dict)
    resp = RestClient.Add(dict)
    print(resp.status_code)


'''
nyBil = {"model": "V80", "stelNummer": "vv.35.68.910", "km": 234500, "aar": 2017, "maerke": "Volvo", "braendsel": "benzin"}
print(nyBil)
resp = RestClient.Add(nyBil)
print(resp.status_code)


biler,resp = RestClient.GetAll()
for b in biler:
    print(b)
'''

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', RECEIVER_TO_PORT))     # (ip, port)

while True:
    buf = s.recv(BUFFER_SIZE)
    #x = threading.Thread(target=do_client(buf), args=(1,))
    #x.start()
    do_client(buf)
