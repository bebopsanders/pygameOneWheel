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
        self.pos = vec(WIDTH/2,HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
