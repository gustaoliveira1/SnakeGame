import sys
import pygame
from lib.berry import Berry
from lib.snake import Snake
from lib.entity_mediator import EntityMediator
from lib.constants import BLACK_COLOR, WINDOW_HEIGHT, WINDOW_WIDTH, GAME_TICK, SNAKE_INITIAL_POSITION


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.snake = Snake(SNAKE_INITIAL_POSITION)
        self.berry = Berry(EntityMediator.generate_berry_position())

    def run(self) -> None:
        clock = pygame.time.Clock()
        last_pressed_key = None

        while not self.snake.collided:
            clock.tick(GAME_TICK)
            self.window.fill(BLACK_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    last_pressed_key = event.key

            self.snake.move(last_pressed_key)
            self.snake.render(self.window)
            self.berry.render(self.window)

            pygame.display.update()

            EntityMediator.verify_collision(self.snake, self.berry)