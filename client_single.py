import pygame
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

lmao = PathDot((424, 152), (424, 152), (568, 296), 3, False, True)

# for line in lines:
#     print(pygame.draw.line(win, (0, 0, 0), line[0], line[1], width=6))
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
    if level_data == None:
        return
    level = num
    map = TileMap(level_data['map'], spritesheet)
    walls = level_data['walls']
    dots = level_data['dots']
    dots.append(lmao)
    home = level_data['home']
    end = level_data['end']
    coins = level_data['coins']
    checkpoints = level_data['checkpoints']
    p1.set_level(level, home, end, checkpoints)


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
            clock.tick(15)
        else:
            clock.tick(60)
        lc = p1.move(walls, dots, coins)
        if lc:
            load_level(level+1)
        update_dots()
        redrawWindow()

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
                    load_level(level+1)
                