import pygame
from config import Config
class Fantasma:
    dire = [[1, 0, 1], [0, 1, 0], [-1, 0, 3], [0, -1, 2]]
    TILE_SIZE = 4
    def __init__(self, x,y):
        self.endereco = None
        self.x = x *Fantasma.TILE_SIZE
        self.y = y *Fantasma.TILE_SIZE
        pass
    def ler_alien(self, scale):
        resize_width = scale
        resize_height = scale
        config = Config()
        self.endereco = pygame.image.load(config.endereco_img+'/enemies/enemy-icecream.png')
        self.endereco = pygame.transform.scale(self.endereco,(resize_width, resize_height))
        pass