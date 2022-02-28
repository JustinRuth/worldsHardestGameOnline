import pygame
from network import Network
import pickle
from player2 import Player
from dot import Dot
from load import load_map
from spritesheet import Spritesheet
from tiles import *


width = 1280
height = 720
canvas = pygame.Surface((width, height))
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
dots = [Dot(500, 300)]
# dot2 = Dot(300, 300)
spritesheet = Spritesheet('spritesheet.png')
lol = ''
map = TileMap('level1.csv', spritesheet)
# points = [(144, 192), (288, 192), (288, 432), (336, 432), (336, 240), (768, 240), (768, 192), (1008, 192), (1008, 480), (864, 480), (864, 240), (816, 240), (816, 432), (384, 432), (384, 480), (144, 480)]
# lines = [((144, 483), (144, 190)), ((147, 192), (285, 192)), ((288, 190), (288, 435)), ((291, 432), (333, 432)), ((336, 435), (336, 238)), ((339, 240), (765, 240)), ((768, 243), (768, 190)), ((771, 192), (1005, 192)), ((1008, 190), (1008, 483)), ((1005, 480), (867, 480)), ((864, 483), (864, 238)), ((861, 240), (819, 240)), ((816, 238), (816, 435)), ((813, 432), (387, 432)), ((384, 430), (384, 483)), ((381, 480), (147, 480))]
# walls = [pygame.Rect(206, 222, 6, 294), pygame.Rect(211, 222, 139, 6), pygame.Rect(350, 222, 6, 246), pygame.Rect(355, 462, 43, 6), pygame.Rect(398, 270, 6, 198), pygame.Rect(403, 270, 427, 6), pygame.Rect(830, 222, 6, 54), pygame.Rect(835, 222, 235, 6), pygame.Rect(1070, 222, 6, 294), pygame.Rect(931, 510, 139, 6), pygame.Rect(926, 270, 6, 246), pygame.Rect(883, 270, 43, 6), pygame.Rect(878, 270, 6, 198), pygame.Rect(451, 462, 427, 6), pygame.Rect(446, 462, 6, 54), pygame.Rect(211, 510, 235, 6)]
current_player = -1

def redrawWindow(win, players, walls):
    win.fill((180, 181, 254))
    canvas.fill((180, 181, 254))
    map.draw_map(canvas)
    win.blit(canvas, (64, 32))
    for dot in dots:
        dot.draw(win)
    # dot2.draw(win)
    for player in players:
        player.draw(win)
    for wall in walls:
        pygame.draw.rect(win, (0, 0, 0), wall)
    pygame.draw.rect(win, (0, 0, 0), (862+64, 238+32, 6, 246))
    pygame.display.update()


def main():
    run = True
    n = Network()
    data = n.getP()
    p1 = data[0]
    level = data[1]
    lol = load_map(level)
    walls = lol['walls']
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        data = n.send(p1)
        players = data
        p1.move(walls, players, dots)
        redrawWindow(win, players, walls)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


main()
