import pygame
import pygame_menu
from player2 import Player
from dot import *
from coin import *
from load import load_map
from spritesheet import Spritesheet
from tiles import *

width = 1280
height = 720
canvas = pygame.Surface((width, height))
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
spritesheet = Spritesheet('spritesheet.png')

p1 = None
level = -1
map = None
walls = []
dots = []
home = ()
end = ()
coins = []
run = True
deaths = 0
deathsPrev = 0


def redrawWindow():
    global win, p1, map, walls, coins
    win.fill((180, 181, 254))
    canvas.fill((180, 181, 254))
    map.draw_map(canvas)
    win.blit(canvas, (64, 32))
    for wall in walls:
        pygame.draw.rect(win, (0, 0, 0), wall)
    for coin in coins:
        coin.draw(win)
    for dot in dots:
        dot.draw(win)
    p1.draw(win)
    pygame.display.update()


def update_dots():
    global dots
    for dot in dots:
        try:
            dot.move()
        except:
            pass


def load_level(num):
    global level, map, walls, dots, home, p1, end, coins
    level_data = load_map(num)
    if level_data is None:
        return False
    level = num
    map = TileMap(level_data['map'], spritesheet)
    walls = level_data['walls']
    dots = level_data['dots']
    home = level_data['home']
    end = level_data['end']
    coins = level_data['coins']
    checkpoints = level_data['checkpoints']
    p1.set_level(num, home, end, checkpoints)
    return True


def load_next_level():
    global level
    load_level(level+1)


def play_single(l):
    global p1, level, run, deaths, deathsPrev
    run = True
    clock = pygame.time.Clock()
    p1 = Player(260, 260, 32, 32, (255, 0, 0), 0)
    level = l
    load_level(level)
    while run:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            clock.tick(15)
        else:
            clock.tick(60)
        lc = p1.move(walls, dots, coins)
        if lc:
            print('lc')
            load_next_level()
        update_dots()
        redrawWindow()
        deaths = p1.get_deaths()
        if deaths != deathsPrev:
            deathsPrev = deaths
            print(deaths)

        if keys[pygame.K_ESCAPE]:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYUP:
                if keys[pygame.K_j]:
                    load_level(level-1)
                if keys[pygame.K_k]:
                    load_next_level()
