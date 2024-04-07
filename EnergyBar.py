import pygame

class EnergyBar:
    def __init__(self, x, y, width, height, color=(255, 165, 0), border_color=(0, 0, 0), border_width=2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.border_color = border_color
        self.border_width = border_width
        self.energy = 1

    def update(self, energy):
        self.energy += energy
        if self.energy > 1:
            self.energy = 1

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, self.border_color, pygame.Rect(self.x - self.border_width, self.y - self.border_width, self.width + 2 * self.border_width, self.height + 2 * self.border_width))
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x + self.border_width, self.y + self.border_width + (1 - self.energy) * (self.height - 2 * self.border_width), self.width - 2 * self.border_width, self.energy * (self.height - 2 * self.border_width)))
