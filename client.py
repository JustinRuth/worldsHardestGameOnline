import pygame
from network import Network
import pickle
from player2 import Player
from dot import *
from load import load_map
from spritesheet import Spritesheet
from tiles import *
from _thread import *


width = 1280
height = 720
canvas = pygame.Surface((width, height))
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
spritesheet = Spritesheet('spritesheet.png')

n = Network()
players = []
p1 = None
level = -1
map = None
walls = []
# dots = []
home = ()


lines = [((480, 435), (480, 190)), ((483, 192), (525, 192)), ((528, 190), (528, 243)), ((531, 240), (669, 240)), ((672, 238), (672, 435)), ((669, 432), (483, 432))]
dot1  = PathDot((568, 296), (568, 296), (712, 440), 3, True, True)
dot2  = PathDot((616, 296), (568, 296), (712, 440), 3, True, True)
dot3  = PathDot((664, 296), (568, 296), (712, 440), 3, True, True)
dot4  = PathDot((712, 296), (568, 296), (712, 440), 3, True, True)
dot5  = PathDot((712, 344), (568, 296), (712, 440), 3, True, True)
dot6  = PathDot((712, 392), (568, 296), (712, 440), 3, True, True)
dot7  = PathDot((712, 440), (568, 296), (712, 440), 3, True, True)
dot8  = PathDot((664, 440), (568, 296), (712, 440), 3, True, True)
dot9  = PathDot((616, 440), (568, 296), (712, 440), 3, True, True)
dot10 = PathDot((568, 440), (568, 296), (712, 440), 3, True, True)
dot11 = PathDot((568, 392), (568, 296), (712, 440), 3, True, True)
dot12 = PathDot((568, 344), (568, 296), (712, 440), 3, True, True)
dots = [dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10, dot11]

def redrawWindow(win):
    global p1, players, map, walls
    win.fill((180, 181, 254))
    canvas.fill((180, 181, 254))
    map.draw_map(canvas)
    win.blit(canvas, (64, 32))
    for dot in dots:
        dot.draw(win)
    for player in players:
        if not player.current_player == p1.current_player:
            player.draw(win)
    for wall in walls:
        pygame.draw.rect(win, (0, 0, 0), wall)

    p1.draw(win)
    pygame.display.update()


def update_players(player, clock):
    global players
    while True:
        clock.tick(60)
        players = n.send(player)


def update_dots():
    global dots
    for dot in dots:
        try:
            dot.move()
        except:
            pass


def load_level(num):
    global level, map, walls, dots, home, p1
    level = num
    level_data = load_map(level)
    map = TileMap(level_data['map'], spritesheet)
    walls = level_data['walls']
    # dots = level_data['dots']
    home = level_data['home']
    p1.set_home(home)

#wtf
def main():
    global p1, level
    run = True
    data = n.getP()
    p1 = data[0]
    level = 3#data[1]
    load_level(level)
    clock = pygame.time.Clock()
    start_new_thread(update_players, (p1, clock))
    while run:
        clock.tick(60)
        p1.move(walls, players, dots)
        update_dots()
        redrawWindow(win)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_j]:
            load_level(1)
        if keys[pygame.K_k]:
            load_level(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


main()
