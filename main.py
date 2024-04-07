import pygame
import noise
import numpy as np
import cv2
import math
from Player import Player
from Settings import WIDTH, HEIGHT, SPEED, SCALE, SEED, DISTANCE, MAP_WIDTH, MAP_HEIGHT
from Settings import OCEAN_RANGE, BEACH_RANGE, GRASS_RANGE, MOUNTAIN_RANGE
from fill_chunk import fill_chunk
from EnergyBar import EnergyBar
from Tornado import Tornado

print("SEED:", SEED)

zoom_factor = 1.4

camera_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))

def draw_red_circles_on_white(image, min_distance=50):
    image_array = pygame.surfarray.array3d(image)
    white_pixels = np.where(np.all(image_array == [255, 255, 255], axis=-1))
    red_circles = []
    for x, y in zip(white_pixels[0], white_pixels[1]):
        if any(np.sqrt((x - xc)**2 + (y - yc)**2) < min_distance for xc, yc in red_circles):
            continue
        red_circles.append((x, y))

    return image, red_circles

def main():
    pygame.init()
    score = 0
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    image = pygame.Surface((WIDTH, HEIGHT))

    player = Player(100,100, SPEED)

    clock = pygame.time.Clock()

    chrono = pygame.time.get_ticks()

    fill_chunk(image, MAP_WIDTH, MAP_HEIGHT, SEED, SCALE, OCEAN_RANGE, BEACH_RANGE, GRASS_RANGE, MOUNTAIN_RANGE)
    image, circle_pos = draw_red_circles_on_white(image)

    tornados = [Tornado('./src/tornado.png', 4, 10, 22, pos) for pos in circle_pos]
    energy_bar = EnergyBar(10, 10, 20, 100)

    energy_bar.move(700, 400)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        seconds = (pygame.time.get_ticks() - chrono) / 1000
        screen.blit(image, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("LEFT")
        if keys[pygame.K_RIGHT]:
            player.move("RIGHT")
        player.move_forward()
        player.draw(screen, energy_bar.energy)

        for tornado in tornados:

            player_pos = player.get_pos()
            tornado_pos = tornado.position

            distance = math.sqrt((player_pos[0] - tornado_pos[0])**2 + (player_pos[1] - tornado_pos[1])**2)
            if distance < DISTANCE and tornado.display:
                energy_bar.update(0.8)
                tornado.display = False
                score = score + 1
            tornado.update()
            tornado.draw(screen, tornado.position)

        energy_bar.draw(screen)
        energy_bar.update(-0.003)

        pygame.display.flip()
        if energy_bar.energy <= 0:
            print("Game Over")
            print("Score:", score * seconds)
            print("Game duration in seconds:", seconds)
            break

    pygame.quit()

if __name__ == "__main__":
    main()