import pygame
from network import Network
import pickle
from player2 import Player
from dot import *
from load import load_map
from spritesheet import Spritesheet
from tiles import *
from _thread import *
import random

width = 1280
height = 720
canvas = pygame.Surface((width, height))
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

dot = Dot(50, 50)

# L1 Dots
dot1 = LinearDot((424, 296), (856, 296), 6, True)
dot2 = LinearDot((856, 344), (424, 344), 6, True)
dot3 = LinearDot((424, 392), (856, 392), 6, True)
dot4 = LinearDot((856, 440), (424, 440), 6, True)
dots = [dot1, dot2, dot3, dot4]

# L2 Dots
# dot1 =  LinearDot((376, 246), (376, 486), 4, False)
# dot2 =  LinearDot((424, 486), (424, 246), 4, False)
# dot3 =  LinearDot((472, 246), (472, 486), 4, False)
# dot4 =  LinearDot((520, 486), (520, 246), 4, False)
# dot5 =  LinearDot((568, 246), (568, 486), 4, False)
# dot6 =  LinearDot((616, 486), (616, 246), 4, False)
# dot7 =  LinearDot((664, 246), (664, 486), 4, False)
# dot8 =  LinearDot((712, 486), (712, 246), 4, False)
# dot9 =  LinearDot((760, 246), (760, 486), 4, False)
# dot10 = LinearDot((808, 486), (808, 246), 4, False)
# dot11 = LinearDot((856, 246), (856, 486), 4, False)
# dot12 = LinearDot((904, 486), (904, 246), 4, False)
# dots = [dot, dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10, dot11, dot12]

spritesheet = Spritesheet('spritesheet.png')
lol = None
players = []
map = None
# points = [(144, 192), (288, 192), (288, 432), (336, 432), (336, 240), (768, 240), (768, 192), (1008, 192), (1008, 480), (864, 480), (864, 240), (816, 240), (816, 432), (384, 432), (384, 480), (144, 480)]
# lines = [((144, 483), (144, 190)), ((147, 192), (285, 192)), ((288, 190), (288, 435)), ((291, 432), (333, 432)), ((336, 435), (336, 238)), ((339, 240), (765, 240)), ((768, 243), (768, 190)), ((771, 192), (1005, 192)), ((1008, 190), (1008, 483)), ((1005, 480), (867, 480)), ((864, 483), (864, 238)), ((861, 240), (819, 240)), ((816, 238), (816, 435)), ((813, 432), (387, 432)), ((384, 430), (384, 483)), ((381, 480), (147, 480))]
# walls = [pygame.Rect(206, 222, 6, 294), pygame.Rect(211, 222, 139, 6), pygame.Rect(350, 222, 6, 246), pygame.Rect(355, 462, 43, 6), pygame.Rect(398, 270, 6, 198), pygame.Rect(403, 270, 427, 6), pygame.Rect(830, 222, 6, 54), pygame.Rect(835, 222, 235, 6), pygame.Rect(1070, 222, 6, 294), pygame.Rect(931, 510, 139, 6), pygame.Rect(926, 270, 6, 246), pygame.Rect(883, 270, 43, 6), pygame.Rect(878, 270, 6, 198), pygame.Rect(451, 462, 427, 6), pygame.Rect(446, 462, 6, 54), pygame.Rect(211, 510, 235, 6)]
# lines = [((144, 387), (144, 286)), ((147, 288), (285, 288)), ((288, 291), (288, 190)), ((291, 192), (861, 192)), ((864, 190), (864, 291)), ((867, 288), (1005, 288)), ((1008, 286), (1008, 387)), ((1005, 384), (867, 384)), ((864, 382), (864, 483)), ((861, 480), (291, 480)), ((288, 483), (288, 382)), ((285, 384), (147, 384))]
walls = [pygame.Rect(206, 318, 6, 102), pygame.Rect(211, 318, 139, 6), pygame.Rect(350, 222, 6, 102), pygame.Rect(355, 222, 571, 6), pygame.Rect(926, 222, 6, 102), pygame.Rect(931, 318, 139, 6), pygame.Rect(1070, 318, 6, 102), pygame.Rect(931, 414, 139, 6), pygame.Rect(926, 414, 6, 102), pygame.Rect(355, 510, 571, 6), pygame.Rect(350, 414, 6, 102), pygame.Rect(211, 414, 139, 6)]
current_player = -1

def redrawWindow(win, p1, players, map, walls):
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


def update_dots():
    for dot in dots:
        try:
            dot.move()
        except:
            pass

def main():
    run = True
    p1 = Player(260, 260, 32, 32, (255, 0, 0), 0)
    level = 1
    lol = load_map(level)
    walls = lol['walls']
    # home = lol['home']
    # p1.home = home
    # p1.x = p1.home[0]
    # p1.y = p1.home[1]
    # p1.update()
    # map = TileMap(f'level{level}.csv', spritesheet)
    map = TileMap(lol['map'], spritesheet)
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p1.move(walls, players, dots)
        update_dots()
        redrawWindow(win, p1, players, map, walls)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


main()
