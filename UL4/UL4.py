# Francis Quentin Mäkinen
import pygame, random, sys
pygame.init()
screen = pygame.display.set_mode([640, 480]) # Teeb 640x480 suuruse akna
pygame.display.set_caption("ÜL4 - Francis Quentin Mäkinen") # Määrab akna nime
clock = pygame.time.Clock() # Kella lisamine

# Skoor
score = 0 # Algseks skooriks on 0
score_font = pygame.font.Font(None, 30) # Skoori font ja selle suurus

# Laeb tausta
bg = pygame.image.load("bg_rally.jpg")
screen.blit(bg,[0,0])

# Laeb autod
car_blue = pygame.image.load("f1_blue.png") # Laeb sinise auto pildi
car_blue2 = pygame.image.load("f1_blue.png") # Laeb teise sinise auto pildi
car_red = pygame.image.load("f1_red.png") # Laeb punase auto pildi

# Asukoht ja kiirus
posX_blue, posY_blue = 175, 0 # Sinise auto X ja Y väärtised
posX_blue2, posY_blue2 = 420, 100 # Teise sinise auto X ja Y väärtised
posX_red, posY_red = 300, 400 # Punase auto X ja Y väärtused
speedY_blue = 5 # Siniste autode kiirus
speedY_red = -5 # Punase auto kiirus

# Lisab autod ekraanile
screen.blit(car_blue, (posX_blue, posY_blue)) # Lisab sinise auto ekraanile
screen.blit(car_blue2, (posX_blue2, posY_blue2)) # Lisab teise sinise auto ekraanile

# Tsükkel
gameover = False
while not gameover:
    # fps
    clock.tick(60)
    # Mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()

    # Auto lisamine ekraanile
    screen.blit(car_red, (posX_red,posY_red))
    screen.blit(car_blue, (posX_blue,posY_blue))
    screen.blit(car_blue2, (posX_blue2,posY_blue2))

    posY_red += speedY_red # Punase auto liikumise tsükkel
    posY_blue += speedY_blue # Esimese sinise auto liikumise tsükkel
    posY_blue2 += speedY_blue # Teise auto liikumise tsükkel
    
    # Autode tagasi liikumine 
    if posY_blue >= 480: # Kui auto positsiooni väärtuseks on arv suurem kui ekraani max suurus(ekraanist väljas)
        posY_blue = 0 # Paigutab auto tagasi ülemisse ekraani äärde
        score = score + 1 # Lisab iga ekraanilt väljumise tagant +1 skoori
        
    if posY_red <= 0: # Kui punase auto positsiooni väärtuseks on arv väiksem kui ekraani min suurus(ekraanist väljas)
        posY_red = 480 # Paigutab punase auto tagasi ekraani alumisse äärde
        
    if posY_blue2 >= 480: # Kui auto positsiooni väärtuseks on arv suurem kui ekraani max suurus(ekraanist väljas)
        posY_blue2 = 0 # Paigutab auto tagasi ekraani ülemisse äärde
        score = score + 1 # Lisab iga ekraanilt väljumise tagant +1 skoori
        
    # Skoori näitamine ekraanil
    score_render = score_font.render(str(score), 1, (54, 81, 225,))
    score_pos = [10, 10]
    screen.blit(score_render, score_pos)

    # Graafika kuvamine ekraanil
    pygame.display.flip()
    screen.blit(bg, (0,0))
 
pygame.quit()