#!/bin/python3
import pygame
from constants import *

def main():
    pygame.init()
    
    # Game Timing
    clock = pygame.time.Clock()
    dt = 0

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main Game Loop
    while True:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))

        # Refresh Screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()