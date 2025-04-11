#!/bin/python3
import pygame
from constants import *

def main():
    pygame.init()
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

if __name__ == "__main__":
    main()