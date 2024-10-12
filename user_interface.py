import pygame
import os

from constants import SCREEN_WIDTH

PADDING = 25

class UI():
    def __init__(self, screen: pygame.Surface, lifes: int = 3, score: int = 0) -> None:
        self.__screen = screen
        self.__font = pygame.font.Font(None, size=36)

    def draw_score(self, score) -> None:
        text_surface = self.__font.render(f"Score: {score:0>6}", True, "white")
        font_width, font_height = text_surface.get_size()
        self.__screen.blit(text_surface, pygame.Vector2(SCREEN_WIDTH - font_width - PADDING, font_height))

    def draw_lifes(self, lifes) -> None:
        image = pygame.image.load(os.path.join('assets', 'heart.png'))
        image = pygame.transform.scale(image, (36, 36))
        for i in range(lifes):
            self.__screen.blit(image, (PADDING + i*36, PADDING))

    def draw(self, score: int, lifes: int) -> None:
        self.draw_score(score)
        self.draw_lifes(lifes)
