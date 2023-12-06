import pygame
from config import Config
class Alienigena:
    dire = [[1, 0, 1], [0, 1, 0], [-1, 0, 3], [0, -1, 2]]
    TILE_SIZE = 4
    def __init__(self, x,y):
        self.endereco = None
        self.pos_x = x *Alienigena.TILE_SIZE
        self.pos_y = y *Alienigena.TILE_SIZE
        self.life  =False
        pass
    
    def check_death(self, exp):

        for e in exp:
            for s in e.sectors:
                if int(self.pos_x/Alienigena.TILE_SIZE ) == s[0] and int(self.pos_y / Alienigena.TILE_SIZE) == s[1]:
                    self.life = False
                    return
    
    def ler_alien(self, scale):
        resize_width = scale
        resize_height = scale
        config = Config()
        self.endereco = pygame.image.load(config.endereco_img+'/enemies/enemy-alien.png')
        self.endereco = pygame.transform.scale(self.endereco,(resize_width, resize_height))
        pass