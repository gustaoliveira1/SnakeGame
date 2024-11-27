import random
import pygame
from pygame import Surface
from lib.entity import Entity
from lib.constants import DIRECTIONS, SQUARE_SIZE, PYTHON_YELLOW_COLOR


class Snake(Entity):
    def __init__(self, position: list[int]) -> None:
        super().__init__(position)

        self.size = 1
        self.pixels: list[list[int]] = [position.copy()]
        self.collided = False
        self.direction = (0, -1)

    def move(self, key) -> None:
        if key in DIRECTIONS:
            new_direction = DIRECTIONS[key]
            if (self.direction[0] + new_direction[0], self.direction[1] + new_direction[1]) != (0, 0):
                self.direction = new_direction

        self.position[0] += self.direction[0] * SQUARE_SIZE
        self.position[1] += self.direction[1] * SQUARE_SIZE

        self.pixels.append(self.position.copy())

        if len(self.pixels) > self.size:
            del self.pixels[0]

    def render(self, window: Surface) -> None:
        for pixel in self.pixels:
            x, y = pixel
            pygame.draw.rect(window, PYTHON_YELLOW_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE))
