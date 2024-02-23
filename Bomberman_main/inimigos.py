import pygame
import random
from config import Config

class Inimigos:

    def __init__(self):
        self.endereco = None
        self.pos_x = 5
        self.pos_y = 5 
        self.life  = True
        self.assasino = -1
        self.time = 300
        self.variavel_c = 0
        
        pass
    
    def check_death(self, exp):
        variavel_ctrl = 0
        for e in exp:
            if variavel_ctrl == 1:
                break
            else:
                for s in e.setor:
                    if int(self.pos_x) == s[0] and int(self.pos_y ) == s[1]:
                        variavel_ctrl =1
                        self.pos_x = 0
                        self.pos_y = 0
                        self.life = False
                        self.assasino = e.jogador
                    
    def move(self, grid, clock, list: list):
        tempx = int(self.pos_x )
        tempy = int(self.pos_y )
        map = []

        for i in range(len(grid)):
            map.append([])
            for j in range(len(grid[i])):
                map[i].append(grid[i][j])

        self.time = self.time - clock
        if self.time < 1:
            
            if self.variavel_c == 0:
                if map[tempx+1][tempy] == 0 :
                    self.pos_x += 1
                
            self.variavel_c = random.randint(0,3)
            if self.variavel_c == 1:
                if map[tempx][tempy-1] == 0 :
                    self.pos_y -= 1    
                # left
            if self.variavel_c == 2:
                if map[tempx-1][tempy] == 0 :

                    self.pos_x -=1
                # baixo
            if self.variavel_c ==3:
                if map[tempx][tempy+1] == 0 :

                    self.pos_y+= 1  

            
                # top
                    
            self.time = 300
                
    def carregar(self, scale, endereco):
        config = Config()
        self.endereco = pygame.image.load(config.endereco_img+endereco)
        self.endereco = pygame.transform.scale(self.endereco,(scale, scale))
        
    def ativar_vida(self):
        self.life = True