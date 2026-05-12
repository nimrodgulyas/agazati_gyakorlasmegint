import random

def kozte(szam1, szam2, szam3):
    if szam1 >= szam2 and szam1 <= szam3:
        return True
    else:
        return False  
  
dobasok = []
hany_darab = 0
for i in range(150):
    i = random.randint(1,12)
    dobasok.append(i)
    
    if kozte(i, 4, 8) == True:
        hany_darab += 1

hany_szazaleka = hany_darab / 150 * 100
print(f"A 150 dobásból {hany_darab} esett 4 és 8 közé.")
print(f'Ez az összes dobás {round(hany_szazaleka, 2)}%-a')