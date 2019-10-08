from kapi import Kapi

kapilar = []

for x in range(100):
    kapi = Kapi(x+1, False)
    kapilar.append(kapi)

for y in range(1, 101):    
    for z in range(y-1, 100, y):        
        kapilar[z].acikMi = not (kapilar[z].acikMi)        

acikKapilar = []

for kapi in kapilar:
    if kapi.acikMi:
        acikKapilar.append(kapi)

for kapi in acikKapilar:
    print(kapi.kapiNo) 