#Francis Quentin Mäkinen
arvud = [4, 49, 32, 5, 83] # Arvude nimekiri

paaris, paaritud = 0, 0 # Paaris ja paaritud muutujate esialgseks väärtuseks on 0

for i in arvud: # For tsükkel
    if i % 2 == 0:
        paaris += 1 # Kui arv jaguneb kahega inkrementeerib paaris muutuja
        
    else:
        paaritud += 1 # Kui arv ei jagune kahega inkrementeerib  paaritud muutuja
        
print("Paaris arve on järjendis ", paaris) # Prindib mitu paarisarvu on järjendis
print("Paarituid arve on järjendis ", paaritud) # Prindib mitu paaritut arvu on järjendis

