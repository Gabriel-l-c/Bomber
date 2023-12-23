import pygame
import sys
import random
import time

from config import Config
from personagem import Personagem
from mapa import Mapa
from alienigena import Alienigena
from fantasma import Fantasma
from bomba import Bomba
from projetil import Projetil
from explosao import Explosao
from inimigos import Inimigos
from quartel import Quartel

BACKGROUND_COLOR = (107, 142, 35)

config = Config()

GRID_BASE = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Jogo:
    fim_de_tempo = 0
    next_indice = 0
    def __init__(self, surface,scale, n_play):
        self.font = pygame.font.SysFont('Bebas', scale, 1)
        self.surface = surface 
        self.cabou_jogo = False
        self.enemys =[] 
        self.time_enemys = 2000
        self.alien = None
        self.fantasma = None
        self.ene_blocks = []
        self.bombas = []
        self.bombas_img = None
        self.explosao_img = None
        self.explosions = []
        self.projeteis =[]
        self.mapa = Mapa(surface,scale)
        self.player = Personagem(n_play)

        self.carregar_mapa(scale)
        
    def load_enemys(self,scale):
        en00 = Quartel()
        en00.carregar(scale*3,'/enemies/ship.png')
        self.enemys.append(en00)
        
        en01 = Inimigos()
        en01.carregar(scale,'/enemies/enemy-aid.png')
        self.enemys.append(en01)
        
        en02 = Inimigos()
        en02.carregar(scale,'/enemies/enemy-bicudo.png')
        self.enemys.append(en02)
        
        en03 = Inimigos()
        en03.carregar(scale,'/enemies/enemy-baby-bearded.png')
        self.enemys.append(en03)
        
        en04 = Inimigos()
        en04.carregar(scale,'/enemies/enemy-chamaleon.png')
        self.enemys.append(en04)
        
        en05 = Inimigos()
        en05.carregar(scale,'/enemies/enemy-pirate.png')
        self.enemys.append(en05)
        
    
    def en_alien(self,scale):
        en1 = Alienigena(1, 11)
        en1.ler_alien(scale)
        en1.life = True
        self.alien = en1

        pass
    
    def en_fantasma(self,scale):
        en2 = Fantasma(11,1)
        en2.ler_fant(scale)
        en2.life=True
        self.fantasma = en2

        pass

    def draw(self,grid, tile_size, dt):
        
        self.time_enemys = self.time_enemys - dt
        
        self.surface.fill(BACKGROUND_COLOR)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.surface.blit(self.mapa.map_iamges[grid[i][j]], (i * tile_size, j * tile_size, tile_size, tile_size))

#criando os enemigos no centro
        for en in self.enemys:
            if en.life:
                    self.surface.blit(en.endereco,
                        (en.pos_x * (tile_size ), en.pos_y * (tile_size )))
                    
                    if Jogo.next_indice == 5:
                        continue
                    
                    elif self.time_enemys < 1 :
                        Jogo.next_indice += 1
                        self.enemys[Jogo.next_indice].ativar_vida()
                        self.time_enemys = 2000
                            
                    
        
        if self.alien.life:
            self.surface.blit(self.alien.endereco,
                    (self.alien.pos_x * (tile_size ), self.alien.pos_y * (tile_size )))
        if self.fantasma.life:
            self.surface.blit(self.fantasma.endereco,
                    (self.fantasma.pos_x * (tile_size), self.fantasma.pos_y * (tile_size)))
            
        for x in self.bombas:
            self.surface.blit(self.bombas_img, (x.pos_x * tile_size, x.pos_y * tile_size, tile_size, tile_size))
        
        for y in self.explosions:
            for c in y.setor:
                self.surface.blit(self.explosao_img, (c[0] * tile_size, c[1] * tile_size, tile_size, tile_size))
            
        
        for s in range(0,self.player.n_player):
            if self.player.life[s]:
                self.surface.blit(self.player.endereco_img[s],
                (self.player.pos_x[s] * tile_size, self.player.pos_y[s]*tile_size, tile_size, tile_size ))
            else : 
                continue
        
        if self.cabou_jogo :
            if self.player.n_player == 1:
                tf = self.font.render("aperte esc para voltar para o menu", False, (139,69,19), (255,211,155))
                pontuacao = self.font.render("pontuacao jogador 1: "+str(self.player.pontos[0]),False, (205,51,51), (255,211,155) )
                self.surface.blit(tf, (30, 130))
                self.surface.blit(pontuacao, (30,30))
            elif self.player.n_player == 2: 
                tf = self.font.render("aperte esc para voltar para o menu", False, (139,69,19), (255,228,196))
                pontuacao1 = self.font.render("pontuacao jogador 1: "+str(self.player.pontos[0]),False, (139,69,19), (255,228,196) )
                pontuacao2 = self.font.render("pontuacao jogador 2: "+str(self.player.pontos[1]),False, (139,69,19), (255,228,196))
                self.surface.blit(tf, (30, 150))
                self.surface.blit(pontuacao1, (60,30))
                self.surface.blit(pontuacao2, (60,60))
                

        pygame.display.update()
        
    def generate_map(self, grid):
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if grid[i][j] != 0 :
                    continue
                
                elif (i < 3 or i > len(grid) - 4) and (j < 3 or j > len(grid[i]) - 4 ) :
                    continue
                
                elif (i>4 and i<8 and j>4 and j<8):
                    continue
        
                if random.randint(0,9)<8:
                    grid[i][j] = 2
        return
    
    def carregar_mapa(self, tile_size):
        
        grid = [row[:] for row in GRID_BASE]
        self.generate_map(grid)
        
        di = time.time()
        
        
        clock = pygame.time.Clock()
        
    
        explosao = pygame.image.load(config.endereco_img+'/items/fogo.png')
        explosao = pygame.transform.scale(explosao, (tile_size, tile_size))
        self.explosao_img= explosao
        
        self.en_alien(tile_size)
        
        self.en_fantasma(tile_size)
        
        self.player.carrega_img(tile_size)
        
        self.load_enemys(tile_size)
        
        running = True
        self.cabou_jogo = False
        #load bombas
       
        bomb_img = Bomba.load_img(tile_size)
        self.bombas_img= bomb_img
        
        while running:
            
            df = time.time()
            # cronometro = df-di
            dt = clock.tick(12)
            
            self.draw(grid, tile_size,dt)
            
            # if self.cabou_jogo:
            #     running = False
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                        
            self.alien.move(grid, dt)  
            self.fantasma.move(grid,dt) 
            
            for enn in self.enemys:
                if enn.life == True:
                    if self.enemys.index(enn) == 0:
                        continue
                    else:
                        enn.move(grid, dt, self.enemys)
            
            # pygame.draw.circle(self.surface, (128,128,128),(self.fantasma.pos_x* tile_size, self.fantasma.pos_y* tile_size), tile_size/5)
            # self.surface.blit(self.surface, (self.fantasma.pos_x* tile_size, self.fantasma.pos_y* tile_size))
            
            if self.player.n_player <= 1:         
                if self.player.life[0]:
                    keys = pygame.key.get_pressed()
                    #aqui sera passado o  movimento, com : posicao x e y, o "mapa", lista ene_blocks, lista powrerups,
                    if keys[pygame.K_s]:
                        self.player.move(0, 1, grid,0)
                    elif keys[pygame.K_d]:
                        self.player.move(1, 0, grid,0)
                    elif keys[pygame.K_w]:
                        self.player.move(0, -1, grid,0)
                    elif keys[pygame.K_a]:
                        self.player.move(-1, 0, grid,0)
                        
                    elif keys[pygame.K_SPACE]:
                            if self.player.life[0] == True and self.player.bomb_limit[0] != 0 :
                                temp_bomb = self.player.plant_bomb(grid,0)
                                self.bombas.append(temp_bomb)
                                grid[temp_bomb.pos_x][temp_bomb.pos_y] = 0
                                self.player.bomb_limit[0] -= 1
                            else :
                                continue
                
                else : 
                    self.player.endereco_img[0]=None
            else:   
                if self.player.life[0]:
                    keys = pygame.key.get_pressed()
                    #aqui sera passado o  movimento, com : posicao x e y, o "mapa", lista ene_blocks, lista powrerups,
                    if keys[pygame.K_s]:
                        self.player.move(0, 1, grid,0)
                    elif keys[pygame.K_d]:
                        self.player.move(1, 0, grid,0)
                    elif keys[pygame.K_w]:
                        self.player.move(0, -1, grid,0)
                    elif keys[pygame.K_a]:
                        self.player.move(-1, 0, grid,0)
                        
                    elif keys[pygame.K_SPACE]:
                            if self.player.bomb_limit[0] != 0 :
                                temp_bomb = self.player.plant_bomb(grid,0)
                                self.bombas.append(temp_bomb)
                                grid[temp_bomb.pos_x][temp_bomb.pos_y] = 0
                                self.player.bomb_limit[0] -= 1
                            else :
                                continue
                            
                if self.player.life[1]:
                    keys = pygame.key.get_pressed()
                    #aqui sera passado o  movimento, com : posicao x e y, o "mapa", lista ene_blocks, lista powrerups,
                    if keys[pygame.K_DOWN]:
                        self.player.move(0, 1, grid,1)
                    elif keys[pygame.K_RIGHT]:
                        self.player.move(1, 0, grid,1)
                    elif keys[pygame.K_UP]:
                        self.player.move(0, -1, grid,1)
                    elif keys[pygame.K_LEFT]:
                        self.player.move(-1, 0, grid,1)
                        
                    elif keys[pygame.K_0]:
                            if self.player.life[1] == True  :
                                if self.player.bomb_limit[1] != 0:
                                    temp_bomb2 = self.player.plant_bomb(grid, 1)
                                    self.bombas.append(temp_bomb2)
                                    grid[temp_bomb2.pos_x][temp_bomb2.pos_y] = 0
                                    self.player.bomb_limit[1] -= 1
                                else :
                                    continue 
                            else:
                                continue
                # else : 
                #     self.player.endereco_img[1] = None   
                # quando o tempo passar de 120 segundos = fim da partida            
            if  df-di > 120:
                self.cabou_jogo = True
                
           # desenhar o cronometro por tempo e frame 
            # self.surface.blit(self.font.render(str(cronometro), True,(0,0,0)),(10,10))
                
            if self.cabou_jogo == False:
                 self.cabou_jogo = self.Fim_de_jogo()
                    
 
            self.update_bombs(grid, dt)

        self.projeteis.clear()
        self.ene_blocks.clear()
        self.explosions.clear()
        self.enemys.clear()
        Jogo.next_indice = 0
  
                                
      
    def update_bombs(self, grid, dt):
        for b in self.bombas:
            b.update(dt)
            if b.time < 1:
                b.bomber.bomb_limit[b.player] += 1
                grid[b.pos_x][b.pos_y] = 0
                exp_temp = Explosao(b.pos_x, b.pos_y, b.range)
                exp_temp.explode(self.bombas, b)
                exp_temp.clear_sectors(grid, b)
                self.explosions.append(exp_temp)
                # print(b.bomber.pontos[0])
                
        self.player.check_death(self.explosions, self.enemys)
        
        self.alien.check_death(self.explosions)
        self.fantasma.check_death(self.explosions)
        
        
        for en in self.enemys:  
            en.check_death(self.explosions)
            
        for e in self.explosions:
            e.update(dt)
            if e.time < 1:
                self.explosions.remove(e)
                
    def Fim_de_jogo(self):
  
        if self.player.life[0] == False or self.player.life[1]== False:
            for e in self.enemys:
                if e.life == False:
                    if self.enemys.index(e) == 0 :
                        if e.assasino == 0:
                            self.player.pontos[0]+=100
                        else :
                            self.player.pontos[1]+=100
                    else:
                        if e.assasino == 0:
                            self.player.pontos[0]+=10
                            
                        elif e.assasino == 1:
                            self.player.pontos[1]+=10
                else:
                    continue
            if self.alien.assasino == 0:
                self.player.pontos[0]+=10
                
            if self.fantasma.assasino == 0:
                self.player.pontos[0]+=10
                
            if self.alien.assasino == 1:
                self.player.pontos[1]+=10
                
            if self.fantasma.assasino == 1:
                self.player.pontos[1]+=10
                
            return True
            


        return False
