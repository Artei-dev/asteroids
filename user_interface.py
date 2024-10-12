import pygame
import os

class UI():
    def __init__(self, screen: pygame.Surface, lifes: int = 3, score: int = 0) -> None:
        self.__screen = screen
        self.lifes = lifes
        self.score = score

    def draw_score(self) -> None:
        pass

    def draw_lifes(self) -> None:
        image = pygame.image.load(os.path.join('assets', 'heart.png'))
        image = pygame.transform.scale(image, (50, 50))
        for i in range(self.lifes):
            self.__screen.blit(image, (5 + i*50, 5))

    def draw(self) -> None:
        self.draw_score()
        self.draw_lifes()
