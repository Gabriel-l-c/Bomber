import pygame
from config import Config
#from personagem import Personagem
#from personagem import Personagem
# ImportError: cannot import name 'Personagem' from partially initialized module 'personagem' (most likely due to a circular import) (c:\Users\Lenovo\Desktop\Bomber1\Bomberman1\personagem.py)
class Bomba:
    frame = 0

    def __init__(self, r,x, y, map, bombardiadores, player:int):
        self.range = r
        self.pos_x = x
        self.pos_y = y
        self.time = 2000
        self.bomber = bombardiadores
        self.sectors = []
        self.player = player
        
        self.get_range(map)
 
    def update(self, dt):
        self.time = self.time - dt
        
        
    def get_range(self, map):

        self.sectors.append([self.pos_x, self.pos_y])

        for x in range(1, self.range):
            if map[self.pos_x + x][self.pos_y] == 1:
                break
            elif map[self.pos_x + x][self.pos_y] == 0 or map[self.pos_x - x][self.pos_y] == 3:
                self.sectors.append([self.pos_x + x, self.pos_y])
            elif map[self.pos_x + x][self.pos_y] == 2:
                self.sectors.append([self.pos_x + x, self.pos_y])
                break
        for x in range(1, self.range):
            if map[self.pos_x - x][self.pos_y] == 1:
                break
            elif map[self.pos_x - x][self.pos_y] == 0 or map[self.pos_x - x][self.pos_y] == 3:
                self.sectors.append([self.pos_x - x, self.pos_y])
            elif map[self.pos_x - x][self.pos_y] == 2:
                self.sectors.append([self.pos_x - x, self.pos_y])
                break
            
        for x in range(1, self.range):
            if map[self.pos_x][self.pos_y + x] == 1:
                break
            elif map[self.pos_x][self.pos_y + x] == 0 or map[self.pos_x][self.pos_y + x] == 3:
                self.sectors.append([self.pos_x, self.pos_y + x])
            elif map[self.pos_x][self.pos_y + x] == 2:
                self.sectors.append([self.pos_x, self.pos_y + x])
                break
        for x in range(1, self.range):
            if map[self.pos_x][self.pos_y - x] == 1:
                break
            elif map[self.pos_x][self.pos_y - x] == 0 or map[self.pos_x][self.pos_y - x] == 3:
                self.sectors.append([self.pos_x, self.pos_y - x])
            elif map[self.pos_x][self.pos_y - x] == 2:
                self.sectors.append([self.pos_x, self.pos_y - x])
                break
 #carregar a imagems para ser blit            
    def load_img(scale):
        resize_width = scale
        resize_height = scale
        config = Config()
        endereco = pygame.image.load(config.endereco_img+'/items/bomba.png')
        endereco = pygame.transform.scale(endereco,(resize_width, resize_height))
        return endereco