import pygame
from dot import *

class Player:
    def __init__(self, x, y, width, height, color, cp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 3
        self.current_player = cp
        self.home = (x, y)
        self.level = 1
        self.end = None
        self.objects = []
        self.dots = []
        self.coins = []
        self.checkpoints = []
        self.deaths = 0
        self.disable = False

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), self.rect)
        inside_width = self.width/1.6
        side = (self.width-inside_width)/2
        pygame.draw.rect(win, self.color, (self.x+side, self.y+side, inside_width, inside_width))

    def get_collisions(self, objects):
        collisions = []
        for obj in objects:
            if self.rect.colliderect(obj):
                collisions.append(obj)
        return collisions

    def move(self):
        keys = pygame.key.get_pressed()
        self.horizontal_movement(keys)
        self.check_collision_x(keys)
        self.vertical_movement(keys)
        self.check_collision_y(keys)
        self.check_collision_checkpoints()
        self.check_collision_coins()
        self.check_collision_dots()
        self.update()
        return self.check_level_complete()

    def horizontal_movement(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        self.update()

    def vertical_movement(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def check_collision_x(self, keys):
        collisions = self.get_collisions(self.objects)
        for obj in collisions:
            if keys[pygame.K_LEFT]:
                self.x = obj.x + obj.width
            elif keys[pygame.K_RIGHT]:
                self.x = obj.x - self.width

    def check_collision_y(self, keys):
        collisions = self.get_collisions(self.objects)
        for obj in collisions:
            if keys[pygame.K_UP]:
                self.y = obj.y + obj.height
            elif keys[pygame.K_DOWN]:
                self.y = obj.y - self.height

    def check_collision_dots(self):
        for dot in self.dots:
            if isinstance(dot, SpinDotParent):
                if self.check_collision_spindots(dot.dots):
                    break
            elif self.rect.colliderect(dot.hitbox):
                self.kill()
                break

    def check_collision_spindots(self, dots):
        for dot in dots:
            if self.rect.colliderect(dot.hitbox):
                self.kill()
                return True
        return False

    def check_collision_coins(self):
        for coin in self.coins:
            if self.rect.colliderect(coin.hitbox):
                coin.collected = True

    def check_collision_checkpoints(self):
        for cp in self.checkpoints[::-1]:
            if self.rect.colliderect(cp[0]) and not cp[2]:
                self.home = cp[1]
                cp = (cp[0], cp[1], True)

    def set_level(self, level, objects, dots, coins, home, end, cp):
        self.level = level
        self.objects = objects
        self.dots = dots
        self.coins = coins
        self.home = home
        self.end = end
        self.checkpoints = cp
        self.x = self.home[0]
        self.y = self.home[1]
        self.update()

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def get_rect(self):
        return self.rect

    def reset_coins(self):
        for coin in self.coins:
            coin.reset()

    def check_level_complete(self):
        count = 0
        for coin in self.coins:
            if coin.collected is True:
                count += 1
        if count == len(self.coins) and self.rect.colliderect(self.end):
            return True
        else:
            return False

    def kill(self):
        self.x = self.home[0]
        self.y = self.home[1]
        self.reset_coins()
        self.deaths += 1

    def reset_deaths(self):
        self.deaths = 0

    def get_deaths(self):
        return self.deaths

    def set_color(self, color):
        self.color = color