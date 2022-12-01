from RestClient import *

print('prøver CRUD')

print('Alle biler')
biler, resp = GetAll()
print(resp.status_code, resp.reason)
for bil in biler:
    print(bil)

print('En bil')
bil = GetOne('XC345627.456')
print(bil)

print('Opret bil')
nyBil = {'model': 'V80', 'stelNummer': 'vv.345.678.910', 'km': 234500, 'aar': 2017, 'maerke': 'Volvo', 'braendsel': 'benzin'}
resp = Add(nyBil)
print(resp.status_code, resp.reason)
print(resp.content)

print('Opdater bil')
nyBil['km']=255000
resp = Edit(nyBil)
print(resp.status_code, resp.reason)
print(resp.content)

print('Slet bil')
resp = Delete(nyBil['stelNummer'])
print(resp.status_code, resp.reason)
print(resp.content)
