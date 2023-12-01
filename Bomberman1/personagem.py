import pygame
import math

from config import Config
from bomba import Bomba
#from enums.power_up_type import PowerUpTy
config = Config()
class Personagem:
    TILE_SIZE = 4
    pos_x = [4,11]
    pos_y = [4,11]
    direction = [0,0]
    frame =[0,0]
    range =[3,3]
    bomb_limit =[1,1]
    TITLE_SIZE = 4
    def __init__(self, n_player):
        self.endereco_img = []
        self.life = True
        self.n_player = n_player
        self.pos_x = [1*Personagem.TITLE_SIZE,11*Personagem.TITLE_SIZE]
        self.pos_y = [1*Personagem.TITLE_SIZE,11*Personagem.TITLE_SIZE]
        self.direction = [0,0]
        self.frame =[0,0]
        self.range =[3,3]
        self.bomb_limit =[1,1]
        pass

#     def move(self, dx, dy, grid, enemys, power_ups):
#         tempx = int(self.pos_x / Player.TILE_SIZE)
#         tempy = int(self.pos_y / Player.TILE_SIZE)

#         map = []

#         for i in range(len(grid)):
#             map.append([])
#             for j in range(len(grid[i])):
#                 map[i].append(grid[i][j])

#         for x in enemys:
#             if x == self:
#                 continue
#             elif not x.life:
#                 continue
#             else:
#                 map[int(x.pos_x / Player.TILE_SIZE)][int(x.pos_y / Player.TILE_SIZE)] = 2

#         if self.pos_x % Player.TILE_SIZE != 0 and dx == 0:
#             if self.pos_x % Player.TILE_SIZE == 1:
#                 self.pos_x -= 1
#             elif self.pos_x % Player.TILE_SIZE == 3:
#                 self.pos_x += 1
#             return
#         if self.pos_y % Player.TILE_SIZE != 0 and dy == 0:
#             if self.pos_y % Player.TILE_SIZE == 1:
#                 self.pos_y -= 1
#             elif self.pos_y % Player.TILE_SIZE == 3:
#                 self.pos_y += 1
#             return

#         # right
#         if dx == 1:
#             if map[tempx+1][tempy] == 0:
#                 self.pos_x += 1
#         # left
#         elif dx == -1:
#             tempx = math.ceil(self.pos_x / Player.TILE_SIZE)
#             if map[tempx-1][tempy] == 0:
#                 self.pos_x -= 1

#         # bottom
#         if dy == 1:
#             if map[tempx][tempy+1] == 0:
#                 self.pos_y += 1
#         # top
#         elif dy == -1:
#             tempy = math.ceil(self.pos_y / Player.TILE_SIZE)
#             if map[tempx][tempy-1] == 0:
#                 self.pos_y -= 1

#         for pu in power_ups:
#             if pu.pos_x == math.ceil(self.pos_x / Player.TILE_SIZE) \
#                     and pu.pos_y == math.ceil(self.pos_y / Player.TILE_SIZE):
#                 self.consume_power_up(pu, power_ups)

#     #def plant_bomb(self, map):
#       #  b = Bomb(self.range, round(self.pos_x / Player.TILE_SIZE), round(self.pos_y / Player.TILE_SIZE), map, self)
#        # return b

#     def check_death(self, exp):
#         for e in exp:
#             for s in e.sectors:
#                 if int(self.pos_x / Player.TILE_SIZE) == s[0] and int(self.pos_y / Player.TILE_SIZE) == s[1]:
#                     self.life = False

#    # def consume_power_up(self, power_up, power_ups):
#     #    if power_up.type == PowerUpType.BOMB:
#      #       self.bomb_limit += 1
#       #  elif power_up.type == PowerUpType.FIRE:
#        #     self.range += 1

#         #power_ups.remove(power_up)

    def carrega_img(self, scale):
        resize_width = scale
        resize_height = scale
        if self.n_player == 1:
            f1 = pygame.image.load(config.endereco_img+'/chars/pacman-blue.png')
            f1 = pygame.transform.scale(f1, (resize_width, resize_height))
            self.endereco_img.append(f1)
            
        else:
            f1 = pygame.image.load(config.endereco_img+'/chars/pacman-blue.png')
            f1 = pygame.transform.scale(f1, (resize_width, resize_height))
            self.endereco_img.append(f1)
            
            f2 = pygame.image.load(config.endereco_img+'/chars/pacman-white.png')
            f2 = pygame.transform.scale(f2, (resize_width, resize_height))
            self.endereco_img.append(f2)
        
