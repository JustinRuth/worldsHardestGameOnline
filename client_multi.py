import pygame, sys
from network import Network
from player2 import Player
from dot import *
from coin import *
from load import load_map
from spritesheet import Spritesheet
from tiles import *
import threading


width = 1280
height = 720
canvas = pygame.Surface((width, height))
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
spritesheet = Spritesheet('spritesheet.png')
font = pygame.font.Font('fonts/ROGFontsv1.6-Regular.ttf', 36)

n = None
players = []
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
code = 0


def set_network(type):
    global n, p1, level, code
    if n is None:
        n = Network()
    if type == 'host':
        data = n.getP(type)
        p1_data = data[0]
        level = data[1]
        code = data[2]
    else:
        data = n.getP(type)
        p1_data = data[0]
        level = data[1]
        code = data[2]
    p1 = Player(p1_data[0], p1_data[1], 32, 32, (255, 0, 0), p1_data[3])


def redrawWindow():
    global win, p1, players, map, walls, coins, font, deaths, level
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
    # print(f'Players: {players}')
    count = 1
    for player in players:
        if not player[3] == p1.current_player:
            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(1045, (count)*40, 1280, 40))
            win.blit(font.render(f"Player {player[3]}: {player[4]}", False, (255, 255, 255)), (1054, -14+((count)*40)))
            count += 1
            if player[2] == p1.level:
                pygame.draw.rect(win, (0, 0, 0), pygame.Rect(player[0], player[1], 32, 32))
                pygame.draw.rect(win, (0, 0, 255), pygame.Rect(player[0]+6, player[1]+6, 20, 20))
    pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, 0, 1280, 40))
    pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, 680, 1280, 40))
    win.blit(font.render("Exit", False, (255, 255, 255)), (10, -14))
    win.blit(font.render(f"Deaths: {deaths}", False, (255, 255, 255)), (1075, -14))
    win.blit(font.render(f"{level} / 10", False, (255, 255, 255)), (600, -14))
    win.blit(font.render(f"Lobby Code: {code}", False, (255, 255, 255)), (10, 666))
    p1.draw(win)
    pygame.display.update()


def update_players(clock):
    global p1, players, run, level, deaths
    while run:
        clock.tick(60)
        try:
            data = [p1.x, p1.y, level, p1.current_player, deaths]
            players = n.send(data)
            players = sorted(players, key=lambda x: x[4])
        except Exception as e:
            print(f'Error: {e}')


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


def play_multi():
    global p1, level, players, n, run, deaths
    run = True
    clock = pygame.time.Clock()
    threading.Thread(target=update_players,
                     args=(clock,),
                     ).start()
    load_level(level)
    # p1.set_color((255, 0, 0))
    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        if p1.move():
            if not load_level(level+1):# Game Complete
                load_level(1)
        deaths = p1.get_deaths()
        update_dots()
        redrawWindow()

        if keys[pygame.K_ESCAPE]:
            run = False
            n.disconnect()
            n = None

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                n.disconnect()
                n = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 90 and 0 <= mouse[1] <= 40:
                    run = False
                    n.disconnect()
                    n = None
