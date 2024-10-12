import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from user_interface import UI
from groups import asteroids, drawable, updateable, shots


def check_for_collisions(player: Player) -> int:
    score = 0
    for asteroid in asteroids:
        if player.is_colliding(asteroid):
            player.get_damage()

        for shot in shots:
            if shot.is_colliding(asteroid):
                score += 100 - asteroid.radius
                asteroid.split(); shot.kill()
    return score

def main():
    # init
    pygame.init()
    pygame.display.set_caption('SuperAsteroids')

    # UI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ui = UI(screen)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # clock related
    clock = pygame.time.Clock()
    dt = 0

    # Spawns new asteroids
    AsteroidField()

    score = 0
    # Game loop
    while player.lifes != 0:
        screen.fill("black")

        score += check_for_collisions(player)

        for obj in updateable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        ui.draw(score=score, lifes=player.lifes)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
