#import pygame 
from pygame import *
from time import time as timer
from random import randint
window = display.set_mode((700, 500))
FPS = 60
display.set_caption('4')
speed_ballx = 3
speed_bally = 3
game = True
finish = False
font.init()
chet1 = 3
chet2 = 3
font = font.Font(None, 35)
lose = font.render('Player1 lose :(', True, (180, 0, 0))
lose2 = font.render('Player2 lose :(', True, (180, 0, 0))
lives1 = font.render(str(chet1), True, (180, 0, 0))
lives2 = font.render(str(chet2), True, (180, 0, 0))

background = transform.scale(image.load('fon.png'), (700, 500))
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
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 595:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 595:
            self.rect.y += self.speed
class Ball_(gameSprite):
    def update(self):
        self.rect.x += speed_ballx
        self.rect.y += speed_bally
 


rocket1 = Player('cloud.png', 100, 250, 15)
rocket2 = Player('cloud.png', 600, 250, 15)
ball = Ball_('myach.png', 350, 250, 15)
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
     
    if not finish:
        window.blit(background, (0, 0))
        window.blit(lives1, (100, 100))
        window.blit(lives2, (600, 100))
        rocket1.update_l()
        rocket2.update_r()
        ball.update()

        rocket1.reset()
        rocket2.reset()
        ball.reset()
        
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_ballx *= -1
        if ball.rect.x < 0:
            chet1 -= 1
            window.blit(lives1, (100, 100))
            if chet1 <= 0:
                finish =  True
                window.blit(lose, (200, 200))
            
        if ball.rect.x > 700:
            chet2 -= 1
            window.blit(lives2, (100, 600))
            if chet2 <= 0:
                finish = True
                window.blit(lose2, (200, 200))
        if ball.rect.y < 50:
            speed_bally *= -1
    
        if ball.rect.y > 450:
            speed_bally *= -1
        
        if ball.rect.x < 0:
            window.blit(lose, (250, 250))
        if ball.rect.x > 700:
            window.blit(lose2, (250, 250))     
    else:
        
        finish = False
    display.update()
    clock.tick(FPS)



