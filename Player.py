import pygame
import noise
import numpy as np
import math
from Settings import WIDTH, HEIGHT, SPEED

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = 90
        self.sprite = pygame.image.load("./src/plane.png")
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.sprites = [pygame.transform.rotate(self.sprite, -i) for i in range(360)]
        self.sprite = self.sprites[self.angle + 90]


    def get_pos(self):
        return self.x, self.y

    def move(self, direction):
        if direction == "LEFT":
            self.angle -= 5  % 360
        elif direction == "RIGHT":
            self.angle += 5 % 360

        self.sprite = self.sprites[(self.angle + 90) % 360]


        dx = self.speed * math.cos(math.radians(self.angle))
        dy = self.speed * math.sin(math.radians(self.angle))

        self.x += dx
        self.y += dy

    def move_forward(self):
        dx = self.speed * math.cos(math.radians(self.angle))
        dy = self.speed * math.sin(math.radians(self.angle))

        self.x += dx
        self.y += dy

    def draw(self, surface, size):

        scaled_sprite = pygame.transform.scale(self.sprite, (int(self.sprite.get_width() * size), int(self.sprite.get_height() * size)))

        sprite_x = self.x - self.sprite.get_width() / 2
        sprite_y = self.y - self.sprite.get_height() / 2

        surface.blit(scaled_sprite, (sprite_x, sprite_y))