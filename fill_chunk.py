import noise
import numpy as np
import pygame

def fill_chunk(image, WIDTH, HEIGHT, SEED, SCALE, OCEAN_RANGE, BEACH_RANGE, GRASS_RANGE, MOUNTAIN_RANGE):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            value = noise.snoise2((x + SEED) * SCALE, (y + SEED) * SCALE)
            color = int((value + 1) / 2 * 255)
            if OCEAN_RANGE(color):
                color = (0, 0, 255)
            elif BEACH_RANGE(color):
                color = (255, 255, 0)
            elif GRASS_RANGE(color):
                color = (0, 255, 0)
            elif MOUNTAIN_RANGE(color):
                color = (255, 255, 255)

            image.fill(color, pygame.Rect(x, y, 1, 1))


