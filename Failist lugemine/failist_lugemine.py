#Francis Quentin Mäkinen
fail = open("sammud.txt", encoding="UTF-8") # Avab faili
kokku = 0 # Kokku esialgseks väärtuseks 0

for rida in fail: # For tsükkel summa saamiseks
    kokku += int(rida)
    
def suurim_failis(fail):  # Funktsioon suurima arvu leidmiseks    
    with open("sammud.txt") as i:        
        data = [int(x) for x in i.readlines()] # Loeb failis ridu, paneb need listi ning data muutuja väärtuseks       
    return max(data) # Tagastab suurima leitud arvu

def vaikseim_failis(fail):  # Funktsioon väikseima arvu leidmiseks    
    with open("sammud.txt") as i:        
        data = [int(x) for x in i.readlines()] # Loeb failis ridu, paneb need listi ning data muutuja väärtuseks       
    return min(data) # Tagastab väikseima leitud arvu

vaikseim_arv = vaikseim_failis(fail) # Paneb väärtuseks väikseima tagastatud arvu
suurim_arv = suurim_failis(fail) # Paneb väärtuseks suurima tagastatud arvu
 
keskmine = kokku / len(rida) # Leiab keskmine jagades summa ridade arvuga
    
fail.close() # Suleb faili

#Prindib kõik andmed
print("See nädal kõnniti", int(kokku), "sammu.")
print("Päevas kõnniti keskmiselt ", int(keskmine), "sammu.")
print("Suurim sammude arv:", suurim_arv)
print("Väikseim sammude arv:", vaikseim_arv)




