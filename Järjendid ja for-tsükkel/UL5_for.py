#Francis Quentin Mäkinen
arvud = [4, 49, 32, 5, 83] # Arvude nimekiri

def arvud_list(arv): # arvud_list fukntsioon, prindib kõik järjendis olevad arvud
    kokku = 0 # Esialgne summa on 0
    for i in arv: # For tsükkel
        kokku += i # Inkremendib kokku muutuja i võrra
        print(kokku) # Prindib järjendi summa
        
if arvud == []: # Kui järjendis pole arve, prindib programm 0
    print(0)
    
print(arvud_list(arvud))

       
