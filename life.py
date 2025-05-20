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
import random

pygame.init()

# Colours and Grid Constants
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

FPS = 60
UPDATE_FREQ = 120                                   # Update every 2 clock cycles

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def gen(num):
    """
    Generates a random set of positions for the grid.
    :param num: Number of positions to generate
    :return: set of random positions, set eliminates duplicates
    """

    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])


def draw_grid(positions):
    """
    Draws the grid in the game window.
    (0,0) is the top left corner of the grid. X and Y increase as you go down and to the right.
    positions are col, row

    :param positions: set of positions to draw
    :return: None
    """

    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))     # *top_left unpacks the tuple

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    for col in range(GRID_WIDTH):
            pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))


def adjust_grid(positions):
    """
    Determine if a pos is active or inactive based on its neighbours
    
    :param positions: 
    :return: 
    """
    all_neighbours = set()
    new_positions = set()

    for position in positions:
        neighbours = get_neighbours(position)       # set eliminates duplicates
        all_neighbours.update(neighbours)

        neighbours = list(filter(lambda x: x in positions, neighbours))

        if len(neighbours) in [2, 3]:               # if an active cell has 2 or 3 neighbours, it remains active
            new_positions.add(position)
                                                    # implicit: if we don't add the pos to the new list, it goes inactive

    for position in all_neighbours:                 # consider the position of all active neighbours
        neighbours = get_neighbours(position)
        neighbours = list(filter(lambda x: x in positions, neighbours))

        if len(neighbours) == 3:                    # if an inactive cell has 3 neighbours, it becomes active
            new_positions.add(position)

    return new_positions


def get_neighbours(pos):
    """
    Retrieve the 8 neighbours of pos.
    Note: the tutorial uses continue statements which I have removed by inverting the logic.

    :param pos: current position
    :return: number of neighbours
    """

    x, y = pos
    neighbours = []
    for dx in [-1, 0, 1]:                           # consider displacement of x and y to the 8 surrounding pos
        if not (x + dx < 0 or x + x + dx > GRID_WIDTH):         # Check that x-pos is on the grid
            for dy in [-1, 0, 1]:
                if not (y + dy <0 or y + dy > GRID_HEIGHT):     # Check that y-pos is on the grid
                    if not (dx == dy == 0):                     # skip the middle position
                        neighbours.append((x + dx, y + dy))     # active neighbours
    return neighbours


#
# Main game loop
#
is_running = True                                   # Boolean switches us is_(verb)
is_playing = False
count = 0
generation = 0
positions = set()

while is_running:
    clock.tick(FPS)                                 # Limit the game loop by limiting the frame rate to FPS
    if is_playing:                                  # Count the clock cycles, FPS is the limit
        count += 1

    if count >= UPDATE_FREQ:                        # When clock exceeds update frequency, redraw the board
        count = 0
        positions = adjust_grid(positions)
        generation += 1

    pygame.display.set_caption(f"Playing, Generation = {generation}" if is_playing else f"Paused, Generation = {generation}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False                      # Exit the game loop when the grid window is closed

        if event.type == pygame.MOUSEBUTTONDOWN:    # Set or unset a tile at the press of any mouse button
            x, y = pygame.mouse.get_pos()
            col = x // TILE_SIZE
            row = y // TILE_SIZE
            pos = (col, row)

            if pos in positions:
                positions.remove(pos)
            else:
                positions.add(pos)

        if event.type == pygame.KEYDOWN:            # Keyboard events
            if event.key == pygame.K_SPACE:         # Spacebar toggles playing the game
                is_playing = not is_playing

            if event.key == pygame.K_c:             # 'C' clears the screen
                positions = set()
                is_playing = False
                count = 0

            if event.key == pygame.K_g:
                positions = gen(random.randrange(2, 5) * GRID_WIDTH)
                generation = 0                      # Reset the generation counter

    screen.fill(GRAY)
    draw_grid(positions)
    pygame.display.update()

pygame.quit()

