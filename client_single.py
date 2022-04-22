import pygame
import pygame_menu
from player2 import Player
from dot import *
from coin import *
from load import load_map
from spritesheet import Spritesheet
from tiles import *

pygame.init()
width = 1280
height = 720
canvas = pygame.Surface((width, height))
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
spritesheet = Spritesheet('spritesheet.png')
font = pygame.font.Font('fonts/ROGFontsv1.6-Regular.ttf', 36)

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


def redrawWindow():
    global win, p1, map, walls, coins, font, deaths, level
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
    pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, 0, 1280, 40))
    win.blit(font.render("Exit", False, (255, 255, 255)), (10, -14))
    win.blit(font.render(f"Deaths: {deaths}", False, (255, 255, 255)), (1075, -14))
    win.blit(font.render(f"{level} / 10", False, (255, 255, 255)), (600, -14))
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
    p1.set_level(num, walls, dots, coins, home, end, checkpoints)
    pygame.time.delay(250)
    return True


def play_single(l):
    global p1, level, run, deaths
    run = True
    clock = pygame.time.Clock()
    p1 = Player(260, 260, 32, 32, (255, 0, 0), 0)
    level = l
    load_level(level)
    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        if p1.move():
            if not load_level(level+1):# Game Complete
                print('lc')
        deaths = p1.get_deaths()
        update_dots()
        redrawWindow()

        if keys[pygame.K_ESCAPE]:
            run = False

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 90 and 0 <= mouse[1] <= 40:
                    run = False