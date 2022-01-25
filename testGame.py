import pygame
from game import Game
from player import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def redrawWindow(win, player):
    win.fill((128,128,128))
    player.draw(win)
    pygame.display.update()

def main():


    player = Player(100, 100, 50, 50, (0, 255, 0), 0)
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.move()
        redrawWindow(win, player)


main()