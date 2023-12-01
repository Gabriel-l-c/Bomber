
import sys 
import pygame
import random 

from enum import Enum

BACKGROUND_COLOR = (107, 142, 35)

font = None

player = None
enemy_list = []
ene_blocks = []
bombs = []
explosions = []
power_ups = []
endereco_base = 'C:/Users/Lenovo/Desktop/Bomberman/Bomberman1/sprites'
GRID_BASE = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

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
        
        # self.carregar_mapa(scale)
        
# #desenhar o mapa com grama, pedras, barricadas
#     def desenhar_mapa(self,grid, tile_size, game_ended ):
#         self.surface.fill(BACKGROUND_COLOR)
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 self.surface.blit(self.map_iamges[grid[i][j]], (i * tile_size, j * tile_size, tile_size, tile_size))
                
#         if game_ended:
#             tf = font.render("Press ESC to go back to menu", False, (153, 153, 255))
#             self.surface.blit(tf, (10, 10))

#         pygame.display.update()
        
# #gerar o mapa com o posicionamento dos personagens
#     def generate_map(self, grid):
#         for i in range(1, len(grid) - 1):
#             for j in range(1, len(grid[i]) - 1):
#                 if grid[i][j] != 0:
#                     continue
#                 elif (i < 3 or i > len(grid) - 4) and (j < 3 or j > len(grid[i]) - 4):
#                     continue
#                 if random.randint(0,9)<7:
#                     grid[i][j] = 2
#         return
    
#     def carregar_mapa(self, tile_size):
#         grid = [row[:] for row in GRID_BASE]
#         self.generate_map(grid)
#         game_ended = False
#         clock = pygame.time.Clock()

#         running = True
#         game_ended = False
#         while running:
#             dt = clock.tick(15)
#             self.desenhar_mapa(grid, tile_size, game_ended)
#             for e in pygame.event.get():
#                 if e.type == pygame.QUIT:
#                     sys.exit(0)
#                 elif e.type == pygame.KEYDOWN:
#                     if e.key == pygame.K_ESCAPE:
#                         running = False

    