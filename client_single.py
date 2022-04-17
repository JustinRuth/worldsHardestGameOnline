import pygame
from player2 import Player
from dot import *
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
run = True

lmao = SpinDotParent((640, 464), 1.75, 5, 36, True)
lmao2 = lmao.dots
def loadDot():
    for dot in lmao2:
        dots.append(dot)

def redrawWindow():
    global win, p1, map, walls
    win.fill((180, 181, 254))
    canvas.fill((180, 181, 254))
    map.draw_map(canvas)
    win.blit(canvas, (64, 32))
    for dot in dots:
        dot.draw(win)
    for wall in walls:
        pygame.draw.rect(win, (0, 0, 0), wall)
    # pygame.draw.rect(win, (0, 0, 0), end)
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
    global level, map, walls, dots, home, p1, end
    level = num
    level_data = load_map(level)
    map = TileMap(level_data['map'], spritesheet)
    walls = level_data['walls']
    dots = level_data['dots']
    loadDot()
    home = level_data['home']
    end = level_data['end']
    p1.set_level(level, home, end)


def play_single(l):
    global p1, level, run
    run = True
    clock = pygame.time.Clock()
    p1 = Player(260, 260, 32, 32, (255, 0, 0), 0)
    level = l
    load_level(level)
    while run:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            clock.tick(1)
        else:
            clock.tick(60)
        lc = p1.move(walls, dots)
        if lc:
            load_level(level+1)
        update_dots()
        redrawWindow()

        if keys[pygame.K_j]:
            load_level(1)
        if keys[pygame.K_k]:
            load_level(2)
        if keys[pygame.K_l]:
            load_level(3)
        if keys[pygame.K_SEMICOLON]:
            load_level(4)
        if keys[pygame.K_ESCAPE]:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                