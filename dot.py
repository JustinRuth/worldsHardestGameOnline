import pygame


class Dot:
    def __init__(self, x, y):
        """Initializes Dot with given values"""
        self.x = x
        self.y = y
        self.radius = 15
        self.color1 = (0, 0, 0)
        self.color2 = (0, 0, 255)
        self.hitbox = pygame.Rect(self.x-11, self.y-11, 22, 22)

    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x-11, self.y-11, 22, 22)

    def draw(self, win):
        """Draws Dot object to Screen"""
        pygame.draw.circle(win, self.color1, (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color2, (self.x, self.y), (self.radius/2)+1)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox)


class LinearDot(Dot):
    def __init__(self, start_pos, end_pos, speed, orientation):
        super().__init__(start_pos[0], start_pos[1])
        if start_pos[0] <= end_pos[0]:
            self.start_pos = start_pos
            self.end_pos = end_pos
        else:
            self.start_pos = end_pos
            self.end_pos = start_pos
        self.speed = speed
        self.orientation = bool(orientation) # True = Horizontal, False = Vertical
        self.direction = True

    def move(self):
        if self.orientation:
            if self.direction:
                if self.x <= self.end_pos[0]:
                    self.update_pos(self.x+self.speed, self.y)
                else:
                    self.direction = False
            else:
                if self.x >= self.start_pos[0]:
                    self.update_pos(self.x-self.speed, self.y)
                else:
                    self.direction = True
        else:
            if self.direction:
                if self.y < self.end_pos[1]:
                    self.update_pos(self.x, self.y+self.speed)
                else:
                    self.direction = False
            else:
                if self.y >= self.start_pos[1]:
                    self.update_pos(self.x, self.y-self.speed)
                else:
                    self.direction = True
        