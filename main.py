import pygame as pg
from settings import *

class Game:
    def __init__(self):
        pass
    def new_game(self):
        pass
    def run_game(self):
        pass
    def events(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
    def main_menu(self):
        pass
    def game_over(self):
        pass
g = Game()
g.main_menu()
while g.running:
    g.new_game()
    g.game_over()
pg.quit()

# About to put the stuff below into my game class 

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    all_sprites.update()
    all_sprites.draw()
    pg.display.flip()
