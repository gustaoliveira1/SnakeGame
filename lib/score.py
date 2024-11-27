import sys
import pygame
from pygame import Surface
from lib.constants import RED_COLOR, WHITE_COLOR, WINDOW_HEIGHT, WINDOW_WIDTH, BACKGROUD
from lib.database_proxy import DatabaseProxy


class Score:
    def __init__(self, window: Surface) -> None:
        self.window = window

    def save(self, score: int) -> None:
        name = ""
        db = DatabaseProxy()

        while True:
            self.window.blit(BACKGROUD, (0, 0))
            self.text(64, "YOU LOST!", RED_COLOR, (WINDOW_WIDTH/2, 100))
            self.text(54, "Enter player name:", WHITE_COLOR, (WINDOW_WIDTH/2, 150))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) <= 10:
                        db.save({ "name": name, "score": score })
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 10 and event.unicode.isprintable():
                            name += event.unicode

            self.text(42, name, WHITE_COLOR, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            pygame.display.update()

    def show(self) -> None:
        db = DatabaseProxy()
        scores = db.get()

        self.window.blit(BACKGROUD, (0, 0))

        self.text(54, "TOP 10 SCORE", WHITE_COLOR, (WINDOW_WIDTH / 2, 50))
        self.text(24, f"{'NAME':<15}{'SCORE':<10}{'DATE':<15}", WHITE_COLOR, (WINDOW_WIDTH / 2, 100))

        for i, value in enumerate(scores):
            id_, name, points, date = value
            formatted_row = f"{name:<15}{points:<10}{date:<15}"
            self.text(24, formatted_row, WHITE_COLOR, (WINDOW_WIDTH / 2, 130 + 30 * i))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()


    def text(self, size: int, text: str, color: tuple, position: tuple) -> None:
        font = pygame.font.Font(size=size)
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=position)
        self.window.blit(surface, rect)