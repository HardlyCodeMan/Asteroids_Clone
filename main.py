#!/bin/python3
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    
    # Game Timing
    clock = pygame.time.Clock()
    dt = 0

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Init Player
    Player.containers = updatable, drawable
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Init Asteroids
    Asteroid.containers = asteroids, updatable, drawable

    # Init Asteroid Field
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    
    # Main Game Loop
    while True:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0))

        # Refresh Screen
        for item in drawable:
            item.draw(screen)
    
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()