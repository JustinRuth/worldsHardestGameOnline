import pygame
from player2 import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win, player, objects):
    win.fill((128, 128, 128))
    player.draw(win)
    for object in objects:
        pygame.draw.rect(win, object[1], object[0])
    pygame.display.update()


def main():
    player = Player(225, 225, 50, 50, (0, 255, 0), 0)
    wall1 = (pygame.Rect(0, 0, 50, 1000), (0, 0, 0))
    wall2 = (pygame.Rect(450, 0, 50, 1000), (0, 0, 0))
    wall3 = (pygame.Rect(0, 0, 1000, 50), (0, 0, 0))
    wall4 = (pygame.Rect(0, 450, 1000, 50), (0, 0, 0))
    wall5 = (pygame.Rect(100, 350, 1000, 50), (0, 0, 0))
    wall6 = (pygame.Rect(0, 100, 400, 50), (0, 0, 0))
    objects = [wall1, wall2, wall3, wall4, wall5, wall6]
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.move(objects)
        redrawWindow(win, player, objects)


main()
