#Francis Quentin Mäkinen
linnad = "Tallinn", "Tartu", "Pärnu", "Viljandi", "Rakvere", "Kuressaare", "Paide" # Koostab linnade nimekirja
a = sorted(linnad) # Sorteerib linnad tähestikulises järjekorras
print(*a, sep = ", ") # Prindib linnade nimekirja, * eemaldab sulud, sep funktsioon lisab komad