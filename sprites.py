import pygame as pg
from settings import *
vec = pg.math.Vector2
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((90,30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        #position
        self.pos = vec(WIDTH/2,HEIGHT/2)
        #velocity
        self.vel = vec(0,0)
        #acceleration
        self.acc = vec(0,0)
    def update(self):
        self.acc = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -0.8
        elif keys[pg.K_d]:
            self.acc.x = 0.8
        elif keys[pg.K_s]:
            self.acc.y = 0.8
        elif keys[pg.K_w]:
            self.acc.y = -0.8
        self.acc += self.vel * -0.12
        self.vel += self.acc
        self.pos += self.acc + 0.5 * self.vel
        self.rect.center = self.pos
