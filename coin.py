import pygame

class Coin:
    def __init__(self, x, y):
        """Initializes Coin with given values"""
        self.x = x
        self.y = y
        self.radius = 12
        self.color1 = (0, 0, 0)
        self.color2 = (255, 255, 0)
        self.hitbox = pygame.Rect(self.x-10, self.y-10, 20, 20)
        self.collected = False

    def draw(self, win):
        """Draws Coin object to Screen"""
        if not self.collected:
            pygame.draw.circle(win, self.color1, (self.x, self.y), self.radius)
            pygame.draw.circle(win, self.color2, (self.x, self.y), (self.radius/2)+1)

    def collect(self):
        self.collected = True

    def reset(self):
        self.collected = False