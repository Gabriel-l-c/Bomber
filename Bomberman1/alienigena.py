import pygame
from config import Config
class Alienigena:
    dire = [[1, 0, 1], [0, 1, 0], [-1, 0, 3], [0, -1, 2]]
    TILE_SIZE = 4
    def __init__(self, x,y):
        self.endereco = None
        self.x = x *Alienigena.TILE_SIZE
        self.y = y *Alienigena.TILE_SIZE
        pass
    
    def ler_alien(self, scale):
        resize_width = scale
        resize_height = scale
        config = Config()
        self.endereco = pygame.image.load(config.endereco_img+'/enemies/enemy-alien.png')
        self.endereco = pygame.transform.scale(self.endereco,(resize_width, resize_height))
        pass