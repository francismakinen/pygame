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
seller = pygame.transform.scale(seller, [300, 350])
screen.blit(seller,[0,0])

pygame.display.flip() # Värskendab akna