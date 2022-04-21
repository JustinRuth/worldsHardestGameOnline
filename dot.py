import pygame
import math

class Dot:
    def __init__(self, x, y):
        """Initializes Dot with given values"""
        self.x = x
        self.y = y
        self.radius = 12
        self.color1 = (0, 0, 0)
        self.color2 = (0, 0, 255)
        self.hitbox = pygame.Rect(self.x-10, self.y-10, 20, 20)

    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x-10, self.y-10, 20, 20)

    def draw(self, win):
        """Draws Dot object to Screen"""
        pygame.draw.circle(win, self.color1, (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color2, (self.x, self.y), (self.radius/2)+1)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox)


class LinearDot(Dot):
    def __init__(self, start_pos, end_pos, speed, orientation):
        super().__init__(start_pos[0], start_pos[1])
        self.orientation = bool(orientation) # True = Horizontal, False = Vertical
        if orientation:
            if start_pos[0] <= end_pos[0]:
                self.start_pos = start_pos
                self.end_pos = end_pos
                self.direction = True
            else:
                self.start_pos = end_pos
                self.end_pos = start_pos
                self.direction = False
        else:
            if start_pos[1] <= end_pos[1]:
                self.start_pos = start_pos
                self.end_pos = end_pos
                self.direction = True
            else:
                self.start_pos = end_pos
                self.end_pos = start_pos
                self.direction = False
        self.speed = speed

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
                if self.y <= self.end_pos[1]:
                    self.update_pos(self.x, self.y+self.speed)
                else:
                    self.direction = False
            else:
                if self.y >= self.start_pos[1]:
                    self.update_pos(self.x, self.y-self.speed)
                else:
                    self.direction = True


class PathDot(Dot):
    def __init__(self, current_pos, tl_pos, br_pos, speed, direction, ReturnDir):
        super().__init__(current_pos[0], current_pos[1])
        self.direction = direction # True = Clockwise, False = CounterClockwise
        self.return_dir = ReturnDir # True = Continue Square, False = Backward Square (L Shape)
        self.speed = speed
        self.tl_pos = tl_pos
        self.br_pos = br_pos
        # self.tr_pos = (br_pos[0], tl_pos[1])
        # self.bl_pos = (tl_pos[0], br_pos[1])
        self.cycle = self.get_cycle()

    def get_cycle(self):
        if self.x == self.tl_pos[0]: # Left
            if self.y == self.tl_pos[1]:
                return 0
            elif self.tl_pos[1] < self.y <= self.br_pos[1]:
                return 3
        elif self.x == self.br_pos[0]: # Right
            if self.y == self.br_pos[1]:
                return 2
            elif self.br_pos[1] > self.y >= self.tl_pos[1]:
                return 1
        elif self.y == self.tl_pos[1]: # Top
            if self.x == self.br_pos[0]:
                return 1
            elif self.br_pos[0] > self.x >= self.tl_pos[0]:
                return 0
        elif self.y == self.br_pos[1]: # Bottom
            if self.x == self.tl_pos[0]:
                return 3
            elif self.tl_pos[0] < self.x <= self.br_pos[0]:
                return 2
        return -1

    def move(self):
        if self.direction:
            if self.cycle == 0:
                self.update_pos(self.x+self.speed, self.y)
                if self.x >= self.br_pos[0]:
                    self.cycle += 1
                    self.x = self.br_pos[0]
            elif self.cycle == 1:
                self.update_pos(self.x, self.y+self.speed)
                if self.y >= self.br_pos[1]:
                    self.cycle += 1
                    self.y = self.br_pos[1]
            elif self.cycle == 2:
                self.update_pos(self.x-self.speed, self.y)
                if self.x <= self.tl_pos[0]:
                    self.cycle += 1
                    self.x = self.tl_pos[0]
            elif self.cycle == 3:
                self.update_pos(self.x, self.y-self.speed)
                if self.y <= self.tl_pos[1]:
                    self.cycle = 0
                    self.y = self.tl_pos[1]
        else:
            if self.cycle == 0:
                self.update_pos(self.x-self.speed, self.y)
                if self.x <= self.tl_pos[0]:
                    self.cycle = 3
                    self.x = self.tl_pos[0]
            elif self.cycle == 1:
                self.update_pos(self.x, self.y-self.speed)
                if self.y <= self.tl_pos[1]:
                    self.cycle -= 1
                    self.y = self.tl_pos[1]
            elif self.cycle == 2:
                self.update_pos(self.x+self.speed, self.y)
                if self.x >= self.br_pos[0]:
                    self.cycle -= 1
                    self.x = self.br_pos[0]
            elif self.cycle == 3:
                self.update_pos(self.x, self.y+self.speed)
                if self.y >= self.br_pos[1]:
                    self.cycle -= 1
                    self.y = self.br_pos[1]


class SpinDotParent():
    def __init__(self, pos, speed, length, separation, offset, center):
        self.x = pos[0]
        self.y = pos[1]
        self.speed = speed
        self.radius = separation
        self.length = length
        self.separation = separation
        self.angle = 0
        self.dots = []
        for i in range(4):
            for u in range(length):
                self.dots.append(SpinDot(pos, speed, (self.radius + offset) + (u * separation), self.angle))
            self.angle += 90
        if center:
            self.dots.append(Dot(pos[0], pos[1]))

    def move(self):
        for dot in self.dots:
            dot.move()

    def draw(self, win):
        for dot in self.dots:
            dot.draw(win)


class SpinDot(Dot):
    def __init__(self, pos, speed, radius, angle):
        super().__init__(pos[0], pos[1])
        self.center = pos
        self.speed = speed
        self.rad = radius
        self.angle = angle

    def move(self):
        x = self.center[0] + math.cos(math.radians(self.angle)) * self.rad
        y = self.center[1] + math.sin(math.radians(self.angle)) * self.rad
        self.update_pos(x, y)
        self.angle += self.speed
