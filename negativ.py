import random

def negativ(szam1):
    if szam1 < 0:
        return True
    else:
        return False
    
mennyi_negativ = 0
for i in range(100):
    i = random.randint(-50, 50)
    if negativ(i) == True:
        mennyi_negativ += 1
        
print(f"A generált számok között {mennyi_negativ} negatív szerepelt.")
    