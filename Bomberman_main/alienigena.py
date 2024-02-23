import pygame
import random
from config import Config
class Alienigena:
    def __init__(self, x,y):
        self.endereco = None
        self.pos_x = x 
        self.pos_y = y 
        self.life  =False
        self.time = 650
        self.assasino = -1
        self.variavel_c = 0
        pass
    
    def check_death(self, exp):
        for e in exp:
            for s in e.setor:
                if int(self.pos_x) == s[0] and int(self.pos_y ) == s[1]:
    
                    self.life = False
                    self.assasino = e.jogador
        
                    
    def move(self, grid, clock):
        tempx = int(self.pos_x )
        tempy = int(self.pos_y )
        map = []

        for i in range(len(grid)):
            map.append([])
            for j in range(len(grid[i])):
                map[i].append(grid[i][j])

        self.time =self.time - clock
        if self.time < 1:
            
            self.variavel_c = random.randint(0,3)
            
            if self.variavel_c == 0:
                if map[tempx+1][tempy] == 0 :
                    self.pos_x += 1
                    self.variavel_c = random.randint(0,3)
                
            
            self.variavel_c = random.randint(0,4)
            if self.variavel_c == 1:
                if map[tempx][tempy-1] == 0 :
                    self.pos_y -= 1    
                # left
            if self.variavel_c == 2 or self.variavel_c == 4:
                if map[tempx-1][tempy] == 0 :

                    self.pos_x -=1
                # baixo
            if self.variavel_c ==3:
                if map[tempx][tempy+1] == 0 :

                    self.pos_y+= 1  

            
                # top
                    
            self.time = 650
                
    def ler_alien(self, scale):
        resize_width = scale
        resize_height = scale
        config = Config()
        self.endereco = pygame.image.load(config.endereco_img+'/enemies/enemy-alien.png')
        self.endereco = pygame.transform.scale(self.endereco,(resize_width, resize_height))
        pass