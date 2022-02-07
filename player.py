import pygame


class Player:
    def __init__(self, x, y, width, height, color, cp):
        """Initializes Player with given values"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 4
        self.current_player = cp

    def draw(self, win):
        """Draws Player object to Screen"""
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        """Detects Keyboard Input and Updates Player Position"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)