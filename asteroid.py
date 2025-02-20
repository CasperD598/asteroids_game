import pygame
import circleshape
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            vector1 = pygame.Vector2.rotate(self.velocity, new_angle)
            vector2 = pygame.Vector2.rotate(self.velocity, -new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_astroid1.velocity = vector1 * 1.2

            new_astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_astroid2.velocity = vector2
