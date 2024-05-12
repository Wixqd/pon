import pygame as pg
import random

l = 5

x_p = 250 # - x игрока
y_p = 450 # - y игрока

x_b = random.randint(0,500)
y_b = random.randint(0,500)

Width = 500
Height = 500
colour = (0 ,0 ,0)

pg.init()
pg.mixer.init()  # для звука
screen = pg.display.set_mode((Width, Height))
pg.display.set_caption("Game")
clock = pg.time.Clock()

running = True
while running:

    pg.time.delay(30)
    screen.fill(colour)
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

#Движение, рисование игрока и блока

# - Игрок
#########################################################################
    player = pg.draw.rect(screen, (0, 250, 154),(x_p, y_p, 10, 10))
    pg.draw.rect(screen, (0, 250, 154),(x_p, y_p, 10, 10)) # - игрок

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        x_p= x_p - 10
    if keys[pg.K_RIGHT]:
        x_p= x_p + 10
    if keys[pg.K_UP]:
        y_p= y_p-10
    if keys[pg.K_DOWN]:
        y_p= y_p+10

    if x_p == 0 and keys[pg.K_LEFT]:
        x_p=+10
    if x_p == 500 and keys[pg.K_RIGHT]:
        x_p= x_p -10
    if y_p == 0 and keys[pg.K_UP]:
        y_p=+10
    if y_p == 500 and keys[pg.K_DOWN]:
        y_p= y_p -10
        
#########################################################################
# - Блок
#########################################################################
    block = pg.draw.rect(screen, (15, 15, 15),(x_b, y_b, 15, 15))
    pg.draw.rect(screen, (15, 15, 15),(x_b, y_b, 15, 15)) # - игрок
    
    if block.colliderect(player):
        x_b = random.randint(0,500)
        y_b = random.randint(0,500)

    pg.display.update()