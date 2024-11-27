import sys
import pygame
import os

if hasattr(sys, '_MEIPASS'):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.abspath(".")

# config
GAME_TICK = 16
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
SQUARE_SIZE = 20
SNAKE_INITIAL_POSITION = [int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2)]
MENU_OPTIONS = (
    "NEW GAME",
    "SCORE",
    "EXIT",
)

DIRECTIONS = {
    # Teclas WASD
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
    # Teclas das setas
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

BACKGROUD_PATH = os.path.join(BASE_PATH, "assets", "images", "background.webp")

BACKGROUD = pygame.transform.scale(
    pygame.image.load(BACKGROUD_PATH), 
    (WINDOW_WIDTH, WINDOW_HEIGHT),
)

# database
DATABASE_PATH = "db.sqlite3"

# colors
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (255, 0, 0)
GRAY_COLOR = (200, 200, 200)
PYTHON_YELLOW_COLOR = (244, 214, 85)