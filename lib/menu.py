import sys
import pygame
from lib.constants import BACKGROUD, GRAY_COLOR, MENU_OPTIONS, WINDOW_HEIGHT, WINDOW_WIDTH, WHITE_COLOR
from lib.game import Game
from lib.score import Score


class Menu:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.option = 0

    def run(self) -> None:
        while True:
            score = Score(self.window)
            data = None

            self.window.blit(BACKGROUD, (0, 0))
            self.text(64, "Snake Game", WHITE_COLOR, (int(WINDOW_WIDTH/2), 100))

            for i in range(len(MENU_OPTIONS)):
                if i == self.option:
                    self.text(36, MENU_OPTIONS[i], GRAY_COLOR, ((WINDOW_WIDTH / 2), 200 + 25 * i))
                else:
                    self.text(36, MENU_OPTIONS[i], WHITE_COLOR, ((WINDOW_WIDTH / 2), 200 + 25 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.handle_menu_navigation(event.key, len(MENU_OPTIONS))

                    if event.key == pygame.K_RETURN:
                        match self.option:
                            case 0:
                                game = Game(self.window)
                                data = game.run()
                            case 1:
                                score.show()
                            case _:
                                pygame.quit()
                                sys.exit()

                if data:
                    score.save(data)

            pygame.display.update()

    def text(self, size: int, text: int, color: tuple, position: tuple) -> None:
        font = pygame.font.Font(size=size)
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=position)
        self.window.blit(surface, rect)

    def handle_menu_navigation(self, key, max_options) -> None:
        match key:
            case pygame.K_w | pygame.K_UP:
                self.option = max(self.option -1, 0)
            case pygame.K_s | pygame.K_DOWN:
                self.option = min(self.option +1, max_options -1)

        return self.option