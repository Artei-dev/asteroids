import pygame
import os

from constants import SCREEN_WIDTH
from player import Player

PADDING = 25

class UI:
    def __init__(self, screen: pygame.Surface) -> None:
        self.__screen = screen
        self.__font = pygame.font.Font(None, size=36)

    def __draw_score(self, score) -> None:
        text_surface = self.__font.render(f"Score: {score:0>6}", True, "white")
        font_width, font_height = text_surface.get_size()
        self.__screen.blit(text_surface, pygame.Vector2(SCREEN_WIDTH - font_width - PADDING, font_height))

    def __draw_lifes(self, lifes) -> None:
        image = pygame.image.load(os.path.join('assets', 'heart.png'))
        image = pygame.transform.scale(image, (36, 36))
        for i in range(lifes):
            self.__screen.blit(image, (PADDING + i*36, PADDING))

    def __draw_untouchable(self, untouchable_timer: int) -> None:
        if untouchable_timer > 0:
            text_surface = self.__font.render(f"Untouchable: {untouchable_timer:.0f}s remaining" , True, "white")
            self.__screen.blit(text_surface, pygame.Vector2(PADDING, 36 + PADDING))

    def draw(self, score: int, player: Player) -> None:
        self.__draw_score(score)
        self.__draw_lifes(player.lifes)
        self.__draw_untouchable(player.untouchable_timer)
