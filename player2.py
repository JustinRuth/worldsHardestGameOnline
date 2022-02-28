import pygame


class Player:
    def __init__(self, x, y, width, height, color, cp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 4
        self.current_player = cp
        self.home = (x, y)

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), self.rect)
        pygame.draw.rect(win, self.color, (self.x+self.width/4, self.y+self.height/4, self.width/2, self.height/2))

    def get_collisions(self, objects, players):
        collisions = []
        for obj in objects:
            if self.rect.colliderect(obj):
                collisions.append(obj)
        for player in players:
            if player.current_player == self.current_player:
                continue
            if self.rect.colliderect(player.rect):
                collisions.append(player.rect)
        return collisions

    def move(self, objects, players, dots):
        keys = pygame.key.get_pressed()
        self.horizontal_movement(keys)
        self.check_collision_x(objects, players, keys)
        self.vertical_movement(keys)
        self.check_collision_y(objects, players, keys)
        self.check_collision_dot(dots)
        self.update()

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

    def check_collision_x(self, objects, players, keys):
        collisions = self.get_collisions(objects, players)
        for obj in collisions:
            if keys[pygame.K_LEFT]:
                self.x = obj.x + obj.width
            elif keys[pygame.K_RIGHT]:
                self.x = obj.x - self.width

    def check_collision_y(self, objects, players, keys):
        collisions = self.get_collisions(objects, players)
        for obj in collisions:
            if keys[pygame.K_UP]:
                self.y = obj.y + obj.height
            elif keys[pygame.K_DOWN]:
                self.y = obj.y - self.height

    def check_collision_dot(self, dots):
        pass

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
