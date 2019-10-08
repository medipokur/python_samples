kapilar = []

for x in range(100):    
    kapilar.append(False)

for y in range(1, 101):    
    for z in range(y-1, 100, y):        
        kapilar[z] = not kapilar[z]

acikKapilar = []

for x in range(100):
    if kapilar[x]:
        acikKapilar.append(x+1)

for y in acikKapilar:
    print(y) 