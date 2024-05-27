import pygame
import math
from queue import PriorityQueue

WIDTH = 800
HEIGHT = WIDTH
ROWS = 50
# NumSpots = 0
Grid = []

def main():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('A* Path Finding')
    window.fill(pygame.Color('white'))

    running = True
    start = None
    end = None

    grid = make_grid(ROWS, WIDTH)
    
    while running:
        draw(window, grid, ROWS, WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]: # Left mouse button pressed
                pos = pygame.mouse.get_pos()

                row, col = get_Clicked_Pos(pos, ROWS, WIDTH)

                spot = grid[row][col]

                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != start and spot != end:
                    spot.make_barrier()

    pygame.quit()

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)

    pygame.display.update()


def draw_grid(win, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))

        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), ( j * gap, width))

def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])

        for j in range(rows):
            spot = Spot(i, j, gap, rows)

            grid[i].append(spot)

    return grid

def get_Clicked_Pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_position(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.colour == RED
    
    def is_open(self):
        return self.colour == GREEN
    
    def is_barrier(self):
        return self.colour == BLACK
    
    def is_start(self):
        return self.colour == ORANGE
    
    def is_end(self):
        return self.colour == TURQUOISE
    
    def reset(self):
        self.colour = WHITE

    def make_start(self):
        self.colour = ORANGE
    
    def make_closed(self):
        self.colour = RED
    
    def make_open(self):
        self.colour = GREEN
    
    def make_barrier(self):
        self.colour = BLACK

    def make_end(self):
        self.colour = TURQUOISE

    def make_path(self):
        self.colour = PURPLE

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        pass

    def __lt__(self, other):
        return False

if __name__ == '__main__':
    main()