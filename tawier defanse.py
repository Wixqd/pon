import pygame
import math
import random

pygame.init()
WIDTH= 800
HEIGHT = 600
FramesPerSecond = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тавер аф хел из роблокса")
bg = pygame.image.load("terka.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

class Castle():
    def __init__(self, x, y, width, height):
        self.health=1000
        self.max_health = self.health
        self.image = pygame.image.load("piza.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.fired = False
    def draw(self):
        screen.blit(self.image, self.rect)
    def shoot(self):
        mouse_pos = pygame.mouse.get_pos()
        x_dist = mouse_pos[0] - self.rect.midleft[0]
        y_dist = -(mouse_pos[1] - self.rect.midleft[1])
        self.angle = math.degrees(math.atan2(y_dist, x_dist))
        pygame.draw.line(screen, (1, 1, 1), (self.rect.centerx, self.rect.centery), (mouse_pos))
        if pygame.mouse.get_pressed()[0]==1:
            self.fired=True
            arrow= Arrow(self.rect.midleft[0], self.rect.midleft[1], self.angle)
            arrows_group.add(arrow)
        if pygame.mouse.get_pressed()[2]==1:
           rx=random.randint(50, 750)
           bomb=Bomb(rx, 100)
           bomb_group.add(bomb)
        if pygame.mouse.get_pressed()[0] == 0:
            self.fired = False


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = math.radians(angle)
        self.speed = 10
        self.dx = math.cos(self.angle)*self.speed
        self.dy = -(math.sin(self.angle)*self.speed)

    def update(self):
        if self.rect.right < 0 or self.rect.left > WIDTH \
                or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()
        self.rect.x += self.dx
        self.rect.y += self.dy
class Bomb(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bomb.png")
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = 10
        self.by = 20
    def update(self, *args, **kwargs):
        self.rect.y +=self.by
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height, health):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
    def update(self):
        for arrow in arrows_group:
            if self.rect.colliderect(arrow.rect):
                arrow.kill
                self.health -=1
                if self.health <=0:
                    self.kill()
        for bomb in bomb_group:
            if self.rect.colliderect(bomb.rect):
                bomb.kill
                self.health -=0.2
                if self.health <=0:
                    self.kill()
        

arrows_group = pygame.sprite.Group()
bomb_group=pygame.sprite.Group()
enemy_group=pygame.sprite.Group()
enemy=Enemy("enemy.png", 100, 500, 125, 175, 500)
enemy_group.add(enemy)

castle = Castle(500, 248, 360, 360)

running = True
while running:
    clock.tick(FramesPerSecond)

    screen.blit(bg, (0, 0))

    castle.draw()
    castle.shoot()
    enemy_group.draw(screen)
    enemy_group.update()
    arrows_group.draw(screen)
    arrows_group.update()
    bomb_group.draw(screen)
    bomb_group.update()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

pygame.quit()