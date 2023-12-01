
import time
import random 
import pygame 

from map import Map 
from utils import load_img


class Pacman:
    def __init__(self, map: Map, size: int, tile_size: int):
        self._pacman_img = load_img("007-pacman\imgs\pacman.png", size=(size, size))
        
        self._map = map
        self._tile_size = tile_size
        self._x = random.randint(0, map.n_cols-1)
        self._y = random.randint(0, map.n_rows-1)

        while map.is_wall(self._x, self._y): 
            self._x = random.randint(0, map.n_cols-1)
            self._y = random.randint(0, map.n_rows-1)

        self._time_last_move = 0
    
    def handle_events(self):
        if time.time() - self._time_last_move < 0.2:
            return
        
        vx = 0
        vy = 0

        if pygame.key.get_pressed()[pygame.K_a]:
            vx = -1
        if pygame.key.get_pressed()[pygame.K_d]:
            vx = 1
        if pygame.key.get_pressed()[pygame.K_s]:
            vy = 1
        if pygame.key.get_pressed()[pygame.K_w]:
            vy = -1
        
        new_x = self._x + vx
        new_y = self._y + vy
        
        if not self._map.is_wall(new_x, new_y):
            self._x = new_x
            self._y = new_y
        
        # (...)
        
        self._map.eat(self._x, self._y)
        
        if vx != 0 or vy != 0:
            self._time_last_move = time.time()
    
    def draw(self, screen: pygame.Surface):
        img_x = self._x * self._tile_size
        img_y = self._y * self._tile_size
        screen.blit(self._pacman_img, (img_x, img_y))
