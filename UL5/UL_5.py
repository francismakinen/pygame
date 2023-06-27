# Francis Quentin Mäkinen
import pygame, random, sys, os
pygame.init()
screen = pygame.display.set_mode([640, 480]) # Teeb 640x480 suuruse akna
color = (144, 238, 144) # color muutujale on antud heleroheline värv
screen.fill(color) # Täidab ekraani color muutujale määratud värviga
pygame.display.set_caption("ÜL4 - Francis Quentin Mäkinen") # Määrab akna nime
clock = pygame.time.Clock() # Kella lisamine
score = 0 # Esialgne skoor on 0
red = [255, 0, 0]

# Palli oordinaadid ja kiirus
ballPos_X = 0 # Palli X koordinaadid
ballPos_Y = 0 # Palli Y koordinaadid
ballSpeed_X = 3 # Palli kiirus X teljel
ballSpeed_Y = 3 # Palli kiirus Y teljel

# Platformi koordinaadid ja kiirus
platformPos_X = 200 # Platformi X koordinaadid
platformPos_Y = 350 # Platformi Y koordinaadid
platformSpeed = 5 # Platformi kiirus


ball = pygame.Rect(ballPos_X, ballPos_Y, 40, 40) # Teeb ball Rect objekti(ristküliku), määrab selle suuruse
pygame.draw.rect(screen, red, ball) # Joonistab ristküliku palli ümber
ballImage = pygame.image.load("ball.png") # Laeb palli pildi 
ballImage = pygame.transform.scale(ballImage, [ball.width, ball.height]) # Muudab palli pildi suurust

platform = pygame.Rect(platformPos_X, platformPos_Y, 230, 40) # Teeb platform Rect objekti, määrab selle suuruse
pygame.draw.rect(screen, red, platform) # Joonistab ristküliku platformi ümber
platformImage = pygame.image.load("pad.png") # Laeb platformi pildi
platformImage = pygame.transform.scale(platformImage, [platform.width, platform.height]) # Muudab platformi pildi suurust

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

    # Objektide kuvamine ekraanil
    platform = pygame.Rect(platformPos_X, platformPos_Y, 230, 40) # Teeb tsüklis platform Rect objekti, määrab selle suuruse
    screen.blit(platformImage, platform) # Platformi kuvamine
    ball = pygame.Rect(ballPos_X, ballPos_Y, 40, 40) # Teeb  tsüklis ball Rect objekti, määrab selle suuruse
    screen.blit(ballImage, ball) # Kuvab palli ekraanil tsüklis
    
    ballPos_X += ballSpeed_X # Palli kiirus X teljel
    ballPos_Y += ballSpeed_Y # Palli kiirus Y teljel
    platformPos_X += platformSpeed # Paneb platformi liikuma lisades iga tsükkel X kordinaatidele 5
    
    # Kokkupõrke tuvastus
    if platformPos_X >= 410: 
        platformSpeed *= -1 
    if platformPos_X == 0:
        platformSpeed += 5  # Kui platform jõuab ekraani paremasse äärde, liigub see vastassuunas tagasi
    if ballPos_X >= 603: 
        ballSpeed_X *= -1 
    if ballPos_X == 0:
        ballSpeed_X += 3 
    if ballPos_Y >= 440:
        ballSpeed_Y *= -1 
    if ballPos_Y == 0:
        ballSpeed_Y += 3 # Kui pall ekraani äärde jõuab, muudab see liikumissuunda
    if ball.colliderect(platform) and ballSpeed_Y > 0: 
        ballSpeed_Y *= -1 
        score += 1 # Kui palli ja platformi ristkülikud puutuvad ja kiirus on üle 0, lisab skoori ja muudab liikumissuunda

    # Skoor
    score_font = pygame.font.Font(None, 30) # Skoori font ja selle suurus
    score_render = score_font.render(str(score), 1, (255, 255, 255,)) # Väljastab skoori väärtuse string-ina, määrab teksti värvi
    score_pos = [10, 10] # Määrab skoori asukoha
    screen.blit(score_render, score_pos) # Kuvab skoori ekraanil

    pygame.display.flip()
    screen.fill(color) # Täidab ekraani värviga

pygame.quit



