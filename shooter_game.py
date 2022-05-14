from pygame import *
from time import time as timer
from random import randint
window = display.set_mode((700, 500))
FPS = 60
display.set_caption('4')
game = True
finish = False
class gameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 30))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(gameSprite):
    def update_l(self):

        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.y < 595:
            self.rect.x += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 595:
            self.rect.x += self.speed

rocket1 = Player('cloud.png', 100, 250, 15)
rocket2 = Player('cloud.png', 600, 250, 15)
ball = gameSprite('myach.png', 350, 250, 15)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
     
    if not finish:
        window.blit(background, (0, 0))
     
    else:
        
        finish = False
    display.update()
    cloak.tick(FPS)


