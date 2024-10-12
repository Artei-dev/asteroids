import pygame
import os

from circleshape import CircleShape
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_STARTING_HEALTH

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.health = PLAYER_STARTING_HEALTH
        self.rotation = 180
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # division is here so that triangle appear squashed
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw_health(self, screen):
        image = pygame.image.load(os.path.join('assets', 'heart.png'))
        image = pygame.transform.scale(image, (50, 50))
        for i in range(self.health):
            screen.blit(image, (5 + i*50, 5))

    def draw(self, screen):
        pygame.draw.polygon(screen, "red", self.triangle(), 2)
        self.draw_health(screen)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if not self.timer > 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN

    def get_damage(self):
        self.health -= 1
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.rotate(dt)
        if keys[pygame.K_r]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer -= dt
