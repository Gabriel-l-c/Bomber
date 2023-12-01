import pygame
import sys
import random

from config import Config
from personagem import Personagem
from mapa import Mapa
from alienigena import Alienigena

BACKGROUND_COLOR = (107, 142, 35)

font = None

player = None
enemy_list = []
ene_blocks = []
bombs = []
explosions = []
power_ups = []

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

class Jogo:
    
    def __init__(self, surface,scale, n_play):
        font = pygame.font.SysFont('Bebas', scale)
        self.surface = surface 
        self.enemys =[] 
        self.bombas = []
        self.projeteis =[]
        self.mapa = Mapa(surface,scale)
        self.player = Personagem(n_play)
        
        self.carregar_mapa(scale)
        

    def en_alien(self,scale):
        en1 = Alienigena(1, 11)
        en1.ler_alien(scale)
        self.enemys.append(en1)
        pass
    def en_fantasma(self,scale):
        pass
    
    def player(self,scale, n_players):
        for w in range(0,n_players):
           
            pass
            
        pass
    
    def draw(self,grid, tile_size, game_ended):
        
        self.surface.fill(BACKGROUND_COLOR)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.surface.blit(self.mapa.map_iamges[grid[i][j]], (i * tile_size, j * tile_size, tile_size, tile_size))
#criando os enemigos em posições expecficas
        for en in self.enemys:
            self.surface.blit(en.endereco,
                   (en.x * (tile_size / 4), en.y * (tile_size / 4)))
        
        if self.player.life:
            for s in range(0,len(self.player.endereco_img)):
                self.surface.blit(self.player.endereco_img[s],
                (self.player.pos_x[s] * (tile_size / 4), self.player.pos_y[s] * (tile_size / 4)))
    
            pass
        
        if game_ended:
            tf = font.render("Press ESC to go back to menu", False, (153, 153, 255))
            self.surface.blit(tf, (10, 10))

        pygame.display.update()
        
    def generate_map(self, grid):
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if grid[i][j] != 0:
                    continue
                elif (i < 3 or i > len(grid) - 4) and (j < 3 or j > len(grid[i]) - 4):
                    continue
                if random.randint(0,9)<7:
                    grid[i][j] = 2
        return
    
    def carregar_mapa(self, tile_size):
        
        grid = [row[:] for row in GRID_BASE]
        self.generate_map(grid)
        
        game_ended = False
        clock = pygame.time.Clock()
        
        self.en_alien(tile_size)
        self.player.carrega_img(tile_size)
        running = True
        game_ended = False
        while running:
            dt = clock.tick(15)
            self.draw(grid, tile_size, game_ended)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False