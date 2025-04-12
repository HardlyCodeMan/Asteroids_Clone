import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            left = self.velocity.rotate(angle)
            right = self.velocity.rotate(-angle)
            new_radius = self.radius / 2
            left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            left_asteroid.velocity = left * 1.2
            right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            right_asteroid.velocity = right * 1.2
        else:
            self.kill()
            return
        
        self.kill()