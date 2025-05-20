"""
     package:   life.py
      author:   Charles J McDonald «https://github.com/cjmcdonald42»
        date:   2025.05.20

The Game of Life was invented by Cambridge mathematician John Conway as a cellular automaton.

This game became widely known when it was mentioned in an article published by Scientific American in 1970. It
consists of a grid of cells which, based on a few mathematical rules, can live, die or multiply. Depending on the
initial conditions, the cells form various patterns throughout the course of the game.
"""

import pygame
pygame.init()

# Colours and Grid Constants
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def main():
    is_running = True
    while is_running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

    pygame.quit()

"""
Only run the main function if this file was explicitly run.
This allows the file to be imported without executing the main function.
"""

if __name__ == "__main__":
    main()

