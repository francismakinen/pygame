#Francis Quentin Mäkinen
import pygame # Impordib PyGame mooduli
pygame.init() # Käivitab PyGame mooduli
screen = pygame.display.set_mode([640, 480]) # Loob akna suurusega 640x480
pygame.display.set_caption("UL3") # Paneb akna nimeks UL3

# Värvid
GREEN = [0, 255, 0] # Määrab rohlise värvi RGB väärtused
RED = [255, 0 ,0] # Määrab punase värvi RGB väärtusted
screen.fill(RED) # Täidab ekraani punase värviga


class Square: # Square klassi loomine
    def __init__(self, color, size1, size2): # color, size1 ja size2 defineerimine
        self.color = color
        self.size1 = size1
        self.size2 = size2
        
    def make_square(self): # Defineerib make_square funktsiooni
        y = 1
        for i in range(35): # Tsükkel i
            x = 1
            for j in range(36): # Tsükkel j
                pygame.draw.rect(screen, self.color, [x, y, self.size1, self.size2]) # Kuni tsükkel jooskeb joonistab ruutusid
                x += 18
            y += 18
            
Square.make_square(Square(GREEN, 10, 10)) # Lubab muuta värvi(praegu GREEN) ning punaste joonte paksust(10)

pygame.display.flip() # Värskendab ekraani

# Programmi ristist kinni panemise funktsioon
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    
pygame.quit() # Sulgeb mängu kui tsükkel lõpeb