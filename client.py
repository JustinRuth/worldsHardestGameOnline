import pygame
from network import Network
import pickle
from player2 import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win, players, walls):
    win.fill((128, 128, 128))
    for player in players:
        player.draw(win)
    for wall in walls:
        pygame.draw.rect(win, wall[1], wall[0])
    pygame.display.update()


def main():
    run = True
    n = Network()
    p1 = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        data = n.send(p1)
        players = data[0]
        walls = data[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move(walls, players)
        redrawWindow(win, players, walls)


main()