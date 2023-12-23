import pygame
import random
from config import Config
from personagem import Personagem
from explosao import Explosao
config = Config()
class Fantasma:
    TILE_SIZE = 4
    def __init__(self, x,y):
        self.endereco = None
        self.pos_x = x
        self.pos_y = y 
        self.life = False
        self.assasino = -1
        self.time = 300
        self.variavel_c = 0
        self.power = -1
        pass
    
    def check_death(self, exp):

        for e in exp:
            for s in e.setor:
                if int(self.pos_x ) == s[0] and int(self.pos_y ) == s[1]:
                    self.life = False
                    self.assasino = e.jogador


                    
    def move(self, grid, clock):
        tempx = int(self.pos_x )
        tempy = int(self.pos_y )
        variavel_c = 0
        map = []
        for i in range(len(grid)):
            map.append([])
            for j in range(len(grid[i])):
                map[i].append(grid[i][j])

        self.time =self.time - clock
        if self.time < 1:
            
            if variavel_c == 0:
                if map[tempx+1][tempy] == 0 or map[tempx+1][tempy] == 2 :
                    self.pos_x += 1
                
            variavel_c = random.randint(0,4)
            if variavel_c == 1:
                if map[tempx][tempy-1] == 0 or map[tempx][tempy-1]==2:
                    self.pos_y -= 1    
         
                # left
            if variavel_c == 2 or variavel_c==4:
                if map[tempx-1][tempy] == 0 or map[tempx-1][tempy]== 2:

                    self.pos_x -=1
                # baixo
            if variavel_c ==3:
                if map[tempx][tempy+1] == 0 or map[tempx][tempy+1]==2:

                    self.pos_y+= 1
 

            
                # top
                    
            self.time = 300
            
    def ler_fant(self, scale):
        resize_width = scale
        resize_height = scale
        config = Config()
        self.endereco = pygame.image.load(config.endereco_img+'/enemies/enemy-skull.png')
        self.endereco = pygame.transform.scale(self.endereco,(resize_width, resize_height))
        self.power = random.randint(0,1)
        pass