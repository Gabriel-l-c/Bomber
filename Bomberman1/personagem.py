import pygame
import math

from config import Config
from bomba import Bomba
#from enums.power_up_type import PowerUpTy
config = Config()
class Personagem:
    TILE_SIZE = 4
    def __init__(self, n_player):
        self.endereco_img = []
        self.life = [True,True]
        self.n_player = n_player
        self.pos_x = [-1,-1]
        self.pos_y = [-1,-1]
        self.direction = [0,0]
        self.frame =[0,0]
        self.range =[5,5]
        self.pontos = [0,0]
        self.bomb_limit = [4,4]
        

    def move(self, dx, dy, grid,  n):
        tempx = int(self.pos_x[n] )
        tempy = int(self.pos_y[n] )

        map = []

        for i in range(len(grid)):
            map.append([])
            for j in range(len(grid[i])):
                map[i].append(grid[i][j])


        # right
        if dx == 1:
            if map[tempx+1][tempy] == 0 or map[tempx+1][tempy]==3:
                self.pos_x[n] += 1
            
        # left
        elif dx == -1:
            if map[tempx-1][tempy] == 0 or map[tempx+1][tempy]== 3:
                self.pos_x[n] -= 1
    

        # bottom
        if dy == 1:
            if map[tempx][tempy+1] == 0 or map[tempx+1][tempy]==3:
                self.pos_y[n] += 1
    
        # top
        elif dy == -1:
            if map[tempx][tempy-1] == 0 or map[tempx+1][tempy]==3:
                self.pos_y[n] -= 1

    def plant_bomb(self, map, n):
       b = Bomba(self.range[n], self.pos_x[n], self.pos_y[n], map, self, n)
       return b

    def check_death(self, exp, enemys:list):
        
        for e in exp:
            for s in e.setor:
                if int(self.pos_x[0]) == s[0] and int(self.pos_y[0]) == s[1]:
                    self.life[0] = False      
                    
                if int(self.pos_x[1]) == s[0] and int(self.pos_y[1]) == s[1]:
                    self.life[1] = False
                    
        # if int(alien.pos_x) == int(self.pos_x[0]) and int(alien.pos_y) == int(self.pos_y[0]) or int(fantasma.pos_x) ==int(self.pos_x[0]) and int(fantasma.pos_y) == int(self.pos_y[0]):
        #     self.life[0] = False
            
        # if int(alien.pos_x) == int(self.pos_x[1]) and int(alien.pos_y) == int(self.pos_y[1])  or int(fantasma.pos_x) ==int(self.pos_x[1]) and int(fantasma.pos_y) == int(self.pos_y[1]):
        #     self.life[1] = False   
            
        for en in enemys:
            if int(self.pos_x[0]) == en.pos_x and int(self.pos_y[0]) == en.pos_y:
                self.life[0] = False  
                
            if int(self.pos_x[1]) == en.pos_x and int(self.pos_y[1]) == en.pos_y:
                self.life[1] = False 
                
    def carrega_img(self, scale):

        
        if self.n_player <= 1:
            f1 = pygame.image.load(config.endereco_img+'/chars/pacman-blue.png')
            f1 = pygame.transform.scale(f1, (scale, scale))
            self.life[0] = True
            self.pos_x[0]=1
            self.pos_y[0]=1
            self.endereco_img.append(f1)
            
        elif self.n_player <=2:
            f1 = pygame.image.load(config.endereco_img+'/chars/pacman-blue.png')
            f1 = pygame.transform.scale(f1, (scale, scale))
            self.life[0] = True
            self.pos_x[0]=1
            self.pos_y[0]=1
            self.endereco_img.append(f1)
               
            f2 = pygame.image.load(config.endereco_img+'/chars/pacman-white.png')
            f2 = pygame.transform.scale(f2,(scale, scale))
            self.life[1]=True
            self.pos_x[1]=11
            self.pos_y[1]=11
            self.endereco_img.append(f2)
        

