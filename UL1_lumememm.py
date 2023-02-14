# Francis Quentin Mäkinen
import pygame # Impordib PyGame mooduli

pygame.init() # Käivitab PyGame mooduli

screen = pygame.display.set_mode([300, 330]) # Loob uue akna suurusega 300x330
pygame.display.set_caption("Lumememm - Francis Makinen") # Paneb akna nimeks Lumememm - Francis MAkinen
pygame.draw.circle(screen, [255, 255, 255], [150, 85], 30, ) # Joonistab esimese valge ringi(screen, värv, koordinaadid, raadius)
pygame.draw.circle(screen, [255, 255, 255], [150, 150], 40, ) # Joonistab teise valge ringi(värv, koordinaadid, raadius)
pygame.draw.circle(screen, [255, 255, 255], [150, 235], 50, ) # Joonistab kolmanda valge ringi(värv, koordinaadid, raadius)
pygame.draw.circle(screen, [0, 0, 0], [140, 80], 5, ) # Joonistab esimese silma(värv, koordinaadid, raadius)
pygame.draw.circle(screen, [0, 0, 0], [160, 80], 5, ) # Joonistab teise silma(värv, koordinaadid, raadius)
pygame.draw.polygon(screen, [255, 0, 0], [[150, 105], [145, 90], [155, 90], [150, 105]], 0) 
# Joonistab kolmnurga.(screen, värv, koordinaadid, joone paksus)

pygame.display.flip() # Värskendab ekraani

# Programmi ristist kinni panemise funktsioon
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    
pygame.quit() # Sulgeb mängu kui tsükkel lõpeb