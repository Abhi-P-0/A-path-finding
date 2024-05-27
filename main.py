import pygame
import math
from queue import PriorityQueue

WIDTH = 800
HEIGHT = WIDTH
# NumSpots = 0
Grid = []

def main():
    NumSpots = input("Grid height (Grid is a square): ")
    PopulateGrid()
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('A* Path Finding')
    window.fill(pygame.Color('white'))

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def PopulateGrid():
    pass



if __name__ == '__main__':
    main()