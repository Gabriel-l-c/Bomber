import pygame
from config import Config

class Quartel:
    def __init__(self):
        self.endereco = None
        self.pos_x = 5
        self.pos_y = 5 
        self.life  = True
        self.vida = [20,20]
        self.assasino = -1
        self.variavel_c = 0
        
    
    def check_death(self, exp):
        variavel_c = 0
        for e in exp:
            if self.variavel_c == 1:
                continue
            else:
                if variavel_c ==0:
                    for s in e.setor:
                        if int(self.pos_x) == s[0] and int(self.pos_y ) == s[1]:
                            variavel_c=1
                            self.vida[e.jogador] -=1
                            
                        if self.vida[e.jogador] == 0:
                            self.variavel_c  =1
                            self.pos_x = - 2
                            self.pos_y = - 2
                            self.life = False
                            self.assasino = e.jogador
        
                    
    def carregar(self, scale, endereco):
        config = Config()
        self.endereco = pygame.image.load(config.endereco_img+endereco)
        self.endereco = pygame.transform.scale(self.endereco,(scale, scale))
        
    def ativar_vida(self):
        self.life = True