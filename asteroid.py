import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color=pygame.Color(255,255,255),
            center=self.position,
            radius=self.radius,
            width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            pass
        
        angle = random.uniform(20, 50)
        
        first_vel = self.velocity.rotate(angle)
        second_vel = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = first_vel * 1.2
        
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = second_vel
        