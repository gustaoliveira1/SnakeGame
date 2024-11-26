import pygame
from pygame import Surface
from lib.entity import Entity
from lib.constants import RED_COLOR, SQUARE_SIZE


class Berry(Entity):
    def __init__(self, position: list[int]) -> None:
        super().__init__(position)

    def render(self, window: Surface) -> None:
        pygame.draw.rect(window, RED_COLOR, (*self.position, SQUARE_SIZE, SQUARE_SIZE))