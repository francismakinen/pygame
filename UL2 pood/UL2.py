#Francis Quentin Mäkinen
import pygame # Impordib PyGame mooduli
pygame.init() # Käivitab PyGame mooduli
screen = pygame.display.set_mode([640, 480]) # Loob akna suurusega 640x480
pygame.display.set_caption("Harjutamine") # Paneb akna nimeks Harjutamine

# Lisab ekraanile taustapildi
bg = pygame.image.load("bg_shop.png") # Laeb taustapildi
screen.blit(bg,[0,0]) # Lisab pildi ekraanile

# Lisab ekraanile müüa
seller = pygame.image.load("seller.png") # Laeb müüja pildi
seller = pygame.transform.scale(seller, [250, 300]) # Muudab pildi suurust
screen.blit(seller,[80,170]) # Muudab pildi paigutust

# Lisab ekraanile jutumulli
chat = pygame.image.load("chat.png") # Laeb jutumulli pildi
screen.blit(chat,[220,50])

# Lisab ekraanile teksti
font = pygame.font.Font(None, 30) # Määrab fondi ja teksti suuruse
text = font.render("Tere, olen Francis", True, [255,255,255]) # Lisab teksti, määrab teksti värvi
screen.blit(text, [270,150]) # Muudab pildi paigutust
pygame.display.flip() # Värskendab akna

# Programmi ristist kinni panemise funktsioon
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    
pygame.quit() # Sulgeb mängu kui tsükkel lõpeb