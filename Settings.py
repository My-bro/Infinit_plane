import noise
import numpy as np

WIDTH = 800
HEIGHT = 600
SPEED = 5

SCALE = 0.01

SEED = np.random.randint(0, 100000)

SPEED = 2

UNIT_SIZE_X = 30
UNIT_SIZE_Y = 70

DISTANCE = 50

MAP_WIDTH = 2000
MAP_HEIGHT = 2000

def OCEAN_RANGE(color):
    return 0 <= color < 170

def BEACH_RANGE(color):
    return 170 <= color < 190

def GRASS_RANGE(color):
    return 190 <= color < 240

def MOUNTAIN_RANGE(color):
    return 240 <= color < 255