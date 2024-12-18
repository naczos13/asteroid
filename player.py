import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIOUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIOUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen,
            color=pygame.Color(255,255,255),
            points=self.triangle(),
            width=2)
        
    def rotate(self, dt):
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        self.shoot_cooldown -= dt
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
            self.shoot(dt)
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self, dt):
        if (self.shoot_cooldown < 0):
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
            s = Shot(self.position.x, self.position.y)
            s.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED