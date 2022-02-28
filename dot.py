import pygame


class Dot:
    def __init__(self, x, y):
        """Initializes Dot with given values"""
        self.pos = (x, y)
        self.radius = 15
        self.color1 = (0, 0, 0)
        self.color2 = (0, 0, 255)
        # self.surface =

    def draw(self, win):
        """Draws Dot object to Screen"""
        pygame.draw.circle(win, self.color1, self.pos, self.radius)
        pygame.draw.circle(win, self.color2, self.pos, (self.radius/2)+1)

