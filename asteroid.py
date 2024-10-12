from sys import setdlopenflags
import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def __create_child(self, angle):
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_vel = self.velocity.rotate(angle)
        smaller_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid.velocity = new_vel * 1.2

    def split(self):
        self.kill()
        if not self.radius == ASTEROID_MIN_RADIUS:
            new_angle = random.uniform(20, 50)

            self.__create_child(new_angle)
            self.__create_child(-new_angle)

    def update(self, dt):
        self.position += self.velocity * dt
