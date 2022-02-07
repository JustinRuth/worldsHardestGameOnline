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

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def get_collisions(self, objects):
        collisions = []
        for object in objects:
            obj = object[0]
            if self.rect.colliderect(obj):
                collisions.append(obj)
        return collisions

    def move(self, objects):
        keys = pygame.key.get_pressed()
        self.horizontal_movement(keys)
        self.check_collision_x(objects, keys)
        self.vertical_movement(keys)
        self.check_collision_y(objects, keys)
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

    def check_collision_x(self, objects, keys):
        collisions = self.get_collisions(objects)
        for obj in collisions:
            if keys[pygame.K_LEFT]:
                self.x = obj.x + obj.width
            elif keys[pygame.K_RIGHT]:
                self.x = obj.x - self.width

    def check_collision_y(self, objects, keys):
        collisions = self.get_collisions(objects)
        for obj in collisions:
            if keys[pygame.K_UP]:
                self.y = obj.y + obj.height
            elif keys[pygame.K_DOWN]:
                self.y = obj.y - self.height

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
