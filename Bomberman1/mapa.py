
import sys 
import pygame
import random 

from enum import Enum
from config import Config
BACKGROUND_COLOR = (107, 142, 35)

font = None

player = None
enemy_list = []
ene_blocks = []
bombs = []
explosions = []
power_ups = []
config = Config()
endereco_base = config.endereco_img


class TileType(Enum):
    WALL = 1 
    EMPTY = 2


class Mapa:
    def __init__(self, surface, scale):
        global font
        global enemy_list
        global ene_blocks
        global player
        global explosions
        global bombs
        global power_ups
        
        self.font = pygame.font.SysFont('Bebas', scale)
        self.player = None
        self.enemy_list = []
        self.ene_blocks = []
        self.bombs = []
        self.explosions = []
        self.power_ups = []
        self.map_iamges = []
        self.surface = surface
        bombs.clear()
        explosions.clear()
        power_ups.clear()


        grass_img = pygame.image.load(endereco_base+'/map/grama.png')
        grass_img = pygame.transform.scale(grass_img, (scale, scale))

        block_img = pygame.image.load(endereco_base+'/map/parede-fixa.png')
        block_img = pygame.transform.scale(block_img, (scale, scale))

        box_img = pygame.image.load(endereco_base+'/map/parede-destruivel.png')
        box_img = pygame.transform.scale(box_img, (scale, scale))

        self.map_iamges = [grass_img,block_img,box_img, grass_img]
        
      