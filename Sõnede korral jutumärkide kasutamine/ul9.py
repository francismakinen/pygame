from tkinter import * # Impordib tkinter mooduli
raam = Tk() # Tekitab uue akna
raam.title("Tühi tahvel") # Paneb programmi nimeks Tühi tahvel
tahvel = Canvas(raam, width=600) # Loob akna laiusega 600 pikslit

tahvel.create_rectangle(50,70,100,100, width=2, outline="blue") # Joonistab sinise ristküliku antud koordinaatidel ja laiusega 2 pixlit
tahvel.create_text(50,50, text="Tere!") # Loob teksti mis ütleb Tere! antud koordinaatidel

tahvel.create_polygon(100,100,150,150,200,100, fill="red", outline="black") # Loob antud koordinaatidel punase kolmnurga mille ümber on must joon

tahvel.pack()
raam.mainloop() # Lõpetab programmi