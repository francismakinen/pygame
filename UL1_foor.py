#Francis Quentin Mäkinen
import pygame # Impordib PyGame mooduli

pygame.init() # Käivitab PyGame mooduli

screen = pygame.display.set_mode([300, 630]) # Loob uue akna suurusega 300x330
pygame.display.set_caption("Foor - Francis Makinen") # Paneb akna nimeks Foor - Francis Makinen

pygame.draw.circle(screen, [255, 0, 0], [150, 85], 35, ) # Joonistab punase ringi(screen, värv, koordinaadid, raadius)
pygame.draw.circle(screen, [255, 255, 0], [150, 160], 35, ) # Joonistab kollase ringi(screen, värv, koordinaadid, raadius)
pygame.draw.circle(screen, [0, 255, 0], [150, 235], 35, ) # Joonistab rohelise ringi(screen, värv, koordinaadid, raadius)

pygame.draw.rect(screen, [128, 128, 128], pygame.Rect(100, 40, 100, 240), 2) # Joonistab ümbritseva ristküliku(screen, värv, koordinaadid ja suurus, paksus)
pygame.draw.rect(screen, [128, 128, 128], pygame.Rect(145, 280, 10, 220), 5) # Joonistab posti(screen, värv, koordinaadid ja suurs, paksus)

pygame.draw.polygon(screen, [128, 128, 128], [[150, 500], [100, 580], [200, 580], [150, 500]], 5) # Joonistab tühja kolmnurga(screen, värv, koordinaadid, paksus)

pygame.draw.polygon(screen, [0, 0, 255], [[150, 500], [135, 525], [165, 525], [150, 500]]) # Joonistab sinise kolmnurga(screen, värv, koordinaadid, paksus)
pygame.draw.polygon(screen, [255, 255, 255], [[120, 550], [100, 580], [200, 580], [180, 550]]) # Joonistab valge kolmnurga(screen, värv, koordinaadid, paksus)


pygame.display.flip() # Värskendab ekraani

# Programmi ristist kinni panemise funktsioon
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    
pygame.quit() # Sulgeb mängu kui tsükkel lõpeb