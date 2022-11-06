from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,sp_image,sp_speed,sp_x,sp_y):
        super().__init__()
        self.image = transform.scale(image.load(sp_image),(65,65))
        self.speed = sp_speed

        self.rect = self.image.get_rect()
        self.rect.x = sp_x
        self.rect.y = sp_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite): # какой нибудь комментарий

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_w - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.x < win_w - 80:
            self.rect.y += self.speed

win_w = 400
win_h = 300

window = display.set_mode((win_w,win_h))
display.set_caption('ping-pong')

while True:
    display.update()
    time.delay(50)
