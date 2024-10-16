import pygame

from circleshape import CircleShape
from groups import shots, updateable, drawable

class Shot(CircleShape):
    containers = (shots, updateable, drawable)

    def __init__(self, x, y):
        super().__init__(x, y, radius=5)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
