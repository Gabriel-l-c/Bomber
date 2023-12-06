import pygame
import sys
import random

from config import Config
from personagem import Personagem
from mapa import Mapa
from alienigena import Alienigena
from fantasma import Fantasma
from power_up import PowerUp
from bomba import Bomba
from projetil import Projetil

BACKGROUND_COLOR = (107, 142, 35)

font = None


GRID_BASE = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 3, 3, 3, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 1],
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
        self.ene_blocks = []
        self.bombas = []
        self.bombas_img = None
        self.projeteis =[]
        self.mapa = Mapa(surface,scale)
        self.player = Personagem(n_play)
        self.power_ups = []
        self.explosiond =[]
        self.carregar_mapa(scale)
        

    def en_alien(self,scale):
        en1 = Alienigena(1, 11)
        en1.ler_alien(scale)
        en1.life = True
        self.enemys.append(en1)
        self.ene_blocks.append(en1)

        pass
    
    def en_fantasma(self,scale):
        en2 = Fantasma(11,1)
        en2.ler_fant(scale)
        en2.life=True
        self.enemys.append(en2)
        self.ene_blocks.append(en2)
        pass
    
    def bombs(self,scale):
        bomb = Bomba()
        pass
    
    def draw(self,grid, tile_size, bomba_img, game_ended):
        
        self.surface.fill(BACKGROUND_COLOR)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.surface.blit(self.mapa.map_iamges[grid[i][j]], (i * tile_size, j * tile_size, tile_size, tile_size))
#criando os enemigos em posições expecficas
        for en in self.enemys:
            self.surface.blit(en.endereco,
                   (en.pos_x * (tile_size / 4), en.pos_y * (tile_size / 4)))
        
        for x in self.bombas:
            self.surface.blit(self.bombas_img, (x.pos_x * tile_size, x.pos_y * tile_size, tile_size, tile_size))
        
        if self.player.life:
            for s in range(0,self.player.n_player):
                self.surface.blit(self.player.endereco_img[s],
                (self.player.pos_x[s] * tile_size, self.player.pos_y[s]*tile_size, tile_size, tile_size ))
    
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
                elif (i < 3 or i > len(grid) - 4) and (j < 3 or j > len(grid[i]) - 4 ) :
                    continue
                if random.randint(0,9)<8:
                    grid[i][j] = 2
        return
    
    def carregar_mapa(self, tile_size):
        
        grid = [row[:] for row in GRID_BASE]
        self.generate_map(grid)
        
        game_ended = False
        clock = pygame.time.Clock()
        
        self.en_alien(tile_size)
        self.en_fantasma(tile_size)
        self.player.carrega_img(tile_size)
        
        running = True
        game_ended = False
        
        #load bombas
       
        bomb_img = Bomba.load_img(tile_size)
        self.bombas_img= bomb_img
        
        while running:
            dt = clock.tick(15)
            self.draw(grid, tile_size, self.bombas_img, game_ended)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                        
            if self.player.n_player <=1:         
                if self.player.life[0]:
                    keys = pygame.key.get_pressed()
                    # = player.direction
                    movement = False
                    if keys[pygame.K_s]:
                        temp = 0
                        self.player.move(0, 1, grid, self.ene_blocks, self.power_ups,0)
                        movement = True
                    elif keys[pygame.K_d]:
                        temp = 1
                        self.player.move(1, 0, grid, self.ene_blocks, self.power_ups,0)
                        movement = True
                    elif keys[pygame.K_w]:
                        temp = 2
                        self.player.move(0, -1, grid, self.ene_blocks, self.power_ups,0)
                        movement = True
                    elif keys[pygame.K_a]:
                        temp = 3
                        self.player.move(-1, 0, grid, self.ene_blocks, self.power_ups,0)
                        movement = True
                        
                    elif keys[pygame.K_SPACE]:
                        for q in range(0, self.player.n_player):
                            if self.player.life[q] == True:
                                temp_bomb = self.player.plant_bomb(grid,(self.player.n_player-1))
                                self.bombas.append(temp_bomb)
                                grid[temp_bomb.pos_x][temp_bomb.pos_y] = 3
                                self.player.bomb_limit[q] -= 1
                        
            # for e in pygame.event.get():
            #     for q in range(0, self.player.n_player-1):
            #         if self.player.life[0] == True:
            #             if e.type == pygame.QUIT:
            #                 sys.exit(0)
            #             elif e.type == pygame.KEYDOWN:
            #                 if e.key == pygame.K_SPACE:
            #                     if self.player.bomb_limit[q] == 0 or not self.player.life[q]:
            #                         continue
            #                     temp_bomb = self.player.plant_bomb(grid,self.player.n_player,tile_size, 0)
            #                     self.bombas.append(temp_bomb)
            #                     grid[temp_bomb.pos_x][temp_bomb.pos_y] = 3
            #                     self.player.bomb_limit[0] -= 1
            #                 elif e.key == pygame.K_ESCAPE:
            #                     running = False
                                
            self.update_bombs(grid, dt)

        self.projeteis.clear()
        self.enemys.clear()
        self.ene_blocks.clear()
        self.power_ups.clear()
                                
            # self.update_bombs(grid, dt)
 
    def update_bombs(self, grid, dt):
        for b in self.bombas:
            b.update(dt)
            if b.time < 1:
                b.bomber.bomb_limit[b.player] += 1
                grid[b.pos_x][b.pos_y] = 0
                exp_temp = Projetil(b.pos_x, b.pos_y, b.range)
                exp_temp.explode(grid, self.bombas, b, self.power_ups)
                exp_temp.clear_sectors(grid, random, self.power_ups)
                self.projeteis.append(exp_temp)
        # if self.player not in self.enemys:
        self.player.check_death(self.projeteis)
        for en in self.enemys:
            en.check_death(self.projeteis)
        for e in self.projeteis:
            e.update(dt)
            if e.time < 1:
                self.projeteis.remove(e)