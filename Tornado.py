import pygame
from Settings import UNIT_SIZE_X, UNIT_SIZE_Y

class Tornado:
    def __init__(self, image_path, frame_count, update_rate, shrink_amount, position):
        self.sprite_sheet = pygame.image.load(image_path)
        self.frame_width = self.sprite_sheet.get_width() // frame_count
        self.frame_height = self.sprite_sheet.get_height()
        self.frames = [pygame.transform.scale(self.sprite_sheet.subsurface(pygame.Rect(i * self.frame_width + shrink_amount // 2, 0, self.frame_width - shrink_amount, self.frame_height)), (UNIT_SIZE_X, UNIT_SIZE_Y)) for i in range(frame_count)]
        self.current_frame = 0
        self.update_rate = update_rate
        self.counter = 0
        self.position = (position[0] - UNIT_SIZE_X // 2, position[1] - UNIT_SIZE_Y // 2)
        self.display = True
        self.x = position[0]
        self.y = position[1]

    def update(self):
        self.counter += 1
        if self.counter >= self.update_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.counter = 0

    def draw(self, surface, position):
        if self.display:
            surface.blit(self.frames[self.current_frame], position)