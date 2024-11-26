import pygame
from pygame import Surface
from lib.entity import Entity
from lib.constants import WHITE_COLOR, SQUARE_SIZE


class Snake(Entity):
    def __init__(self, position: list[int]) -> None:
        super().__init__(position)

        self.size = 1
        self.pixels: list[list[int]] = [position.copy()]
        self.collided = False

    def move(self, key) -> None:
        if key == pygame.K_w:
            self.position[1] -= SQUARE_SIZE
        elif key == pygame.K_s:
            self.position[1] += SQUARE_SIZE
        elif key == pygame.K_a:
            self.position[0] -= SQUARE_SIZE
        elif key == pygame.K_d:
            self.position[0] += SQUARE_SIZE

        self.pixels.append(self.position.copy())

        if len(self.pixels) > self.size:
            del self.pixels[0]

    def render(self, window: Surface) -> None:
        for pixel in self.pixels:
            x, y = pixel
            pygame.draw.rect(window, WHITE_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE))