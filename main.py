import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # init
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups - drawable and updateable
    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    # player related
    Player.containers = (drawable, updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    dt = 0
    while True:
        screen.fill((0, 0, 0))

        for obj in updateable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
