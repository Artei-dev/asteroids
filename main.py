import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from user_interface import UI


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # init
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('SuperAsteroids')

    # groups - drawable and updateable
    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # player related
    Player.containers = (drawable, updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updateable, drawable)

    # UI
    ui = UI(screen)

    dt = 0
    while player.lifes != 0:
        screen.fill("black")
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                player.get_damage()

            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split(); shot.kill()

        for obj in updateable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        ui.lifes = player.lifes
        ui.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
