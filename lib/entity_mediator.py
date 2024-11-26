import random
from lib.constants import WINDOW_HEIGHT, WINDOW_WIDTH, SQUARE_SIZE


class EntityMediator:
    @staticmethod
    def generate_berry_position() -> list[int]:
        x = int(random.randint(0, WINDOW_WIDTH - SQUARE_SIZE) / SQUARE_SIZE) * SQUARE_SIZE
        y = int(random.randint(0, WINDOW_HEIGHT - SQUARE_SIZE) / SQUARE_SIZE) * SQUARE_SIZE
        return x, y

    @staticmethod
    def _vetify_berry_collision(snake, berry) -> None:
        for pixel in snake.pixels:
            pixel_x, pixel_y = pixel
            berry_x, berry_y = berry.position
            if pixel_x == berry_x and pixel_y == berry_y:
                berry.position = EntityMediator.generate_berry_position()
                snake.size += 1

    @staticmethod
    def _verify_border_collision(snake) -> None:
        head_x, head_y = snake.position

        if head_x < 0:
            snake.position[0] = WINDOW_WIDTH - SQUARE_SIZE
        elif head_x >= WINDOW_WIDTH:
            snake.position[0] = 0
        elif head_y < 0:
            snake.position[1] = WINDOW_HEIGHT - SQUARE_SIZE
        elif head_y >= WINDOW_HEIGHT:
            snake.position[1] = 0

    @staticmethod
    def _verify_self_collision(snake) -> None:
        head_x, head_y = snake.position

        for pixel in snake.pixels[:-1]:
            pixel_x, pixel_y = pixel

            if head_x == pixel_x and head_y == pixel_y:
                snake.collided = True

    @staticmethod
    def verify_collision(snake, berry) -> None:
        EntityMediator._vetify_berry_collision(snake, berry)
        EntityMediator._verify_border_collision(snake)
        EntityMediator._verify_self_collision(snake)