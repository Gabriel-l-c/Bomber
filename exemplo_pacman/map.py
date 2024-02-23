
import sys 
import pygame
import random 
from enum import Enum


class TileType(Enum):
    WALL = 1 
    EMPTY = 2
    WITH_FOOD = 3


class Map:
    def __init__(self, n_cols: int, n_rows: int): 
        self._grid = []
        
        self.n_rows = n_rows
        self.n_cols = n_cols
        
        for row_idx in range(n_rows):
            row = []
            for col_idx in range(n_cols):
                if (row_idx == 0) or (row_idx == n_rows - 1) or \
                    (col_idx == 0) or (col_idx == n_cols - 1) or \
                    (random.random() < 0.2):
                    row.append(TileType.WALL)
                else:
                    row.append(TileType.WITH_FOOD)
                    
            self._grid.append(row)

    def draw(self, screen: pygame.Surface, tile_size: int):
        w = h = tile_size
        for row_idx in range(self.n_rows):
            y = row_idx * tile_size
            for col_idx in range(self.n_cols):
                x = col_idx * tile_size
                self._draw_tile(y, x, w, h, screen, self._grid[row_idx][col_idx])

    def is_wall(self, x, y):
        return self._grid[y][x] == TileType.WALL

    def eat(self, x, y):
        if self._grid[y][x] == TileType.WITH_FOOD:
            self._grid[y][x] = TileType.EMPTY

    def _draw_tile(self, y, x, w, h, screen, tile_type):
        if tile_type == TileType.WALL:
            pygame.draw.rect(screen, "blue", pygame.Rect(x, y, w, h))
        elif tile_type == TileType.WITH_FOOD:
            pygame.draw.rect(screen,  "black", pygame.Rect(x, y, w, h))
            center_x = x + w // 2
            center_y = y + w // 2
            pygame.draw.circle(screen, center=(center_x, center_y), radius=4, color="white")
        elif tile_type == TileType.EMPTY:
            pygame.draw.rect(screen,  "black", pygame.Rect(x, y, w, h))
        else:
            print("Unknown tile type")
            sys.exit(-1)
    
