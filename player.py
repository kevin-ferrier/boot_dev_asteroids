import pygame
from pygame import Vector2, draw
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self,x:float, y:float):
        super().__init__(x,y,PLAYER_RADIUS)
        self.position = Vector2(x,y)
        self.rotation = 0
        self.cd = 0

    def draw(self, screen):
        draw.polygon(screen, "white", self.triangle())


    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, delta):
        self.rotation += (PLAYER_TURN_SPEED * delta)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.cd -= dt

    def move(self, delta):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta

    def shoot(self):
        if self.cd <= 0:
            shot = Shot(self.position.x, self.position.y, 2)
            shot.velocity = Vector2(0,1).rotate(self.rotation )* PLAYER_SHOOT_SPEED
            self.cd = PLAYER_SHOOT_COOLDOWN
