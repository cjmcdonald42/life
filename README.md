     package:   life.py
      author:   Charles J McDonald «https://github.com/cjmcdonald42»
        date:   2025.05.20
     version:   1.0
    maturity:   Production

# life
The Game of Life was invented by Cambridge mathematician John Conway as a cellular automaton.

This game became widely known when it was mentioned in an article published by Scientific American in 1970. It
consists of a grid of cells which, based on a few mathematical rules, can live, die or multiply. Depending on the
initial conditions, the cells form various patterns throughout the course of the game.

## Rules
The game is played on a large grid of cells, where each cell can be either alive or dead.

The state of the grid is updated at each step according to the following rules:
1. Each cell with one or no neighbors dies, as if by solitude.
2. Each cell with four or more neighbors dies, as if by overpopulation.
3. Each cell with two or three neighbors survives.
4. Each cell with three neighbors becomes populated.

## Exercise
I've used this program as a learning exercise to practice Python programming. I've followed Tech with Tim's work
(referenced below) to learn how to use the pyGame library and learn how to create a simple simulation game.

## References
1. [John Conway's Game of Life](https://playgameoflife.com)
2. Tech with Tim «https://github.com/techwithtim» "Python Simulation Tutorial - Conway's Game of Life"
[GitHub](https://github.com/techwithtim/Conways-Game-Of-Life), [YouTube](https://www.youtube.com/watch?v=YDKuknw9WGs)

### This work © 2025 by Charles J McDonald is licensed under CC BY-NC-SA 4.0
