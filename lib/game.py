import pygame
from pygame import Surface
from lib.berry import Berry
from lib.snake import Snake
from lib.entity_mediator import EntityMediator
from lib.constants import BLACK_COLOR, GAME_TICK, SNAKE_INITIAL_POSITION, WHITE_COLOR


class Game:
    def __init__(self, window: Surface) -> None:
        self.window = window
        self.snake = Snake(SNAKE_INITIAL_POSITION)
        self.berry = Berry(EntityMediator.generate_berry_position())

    def run(self) -> None:
        clock = pygame.time.Clock()
        last_pressed_key = None

        while not self.snake.collided:
            clock.tick(GAME_TICK)
            self.window.fill(BLACK_COLOR)
            self.text(32, f"Score: {(self.snake.size - 1) * 10}", WHITE_COLOR, (10, 10))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    last_pressed_key = event.key

            self.snake.move(last_pressed_key)
            self.snake.render(self.window)
            self.berry.render(self.window)

            pygame.display.update()

            EntityMediator.verify_collision(self.snake, self.berry)

    def text(self, size: int, text: str, color: tuple, position: tuple) -> None:
        font = pygame.font.Font(size=size)
        surface = font.render(text, True, color)
        rect = surface.get_rect(left=position[0], top=position[1])
        self.window.blit(surface, rect)