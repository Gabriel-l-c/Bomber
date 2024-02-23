from personagem import Personagem
from bomba import Bomba
class Explosao:

    bomber = None

    def __init__(self, x, y, r):
        self.sourceX = x
        self.sourceY = y
        self.range = r
        self.time = 250
        self.frame = 0
        self.setor = []
        self.bomber = None
        self.jogador = -1

    def explode(self, bombs: list, b: Bomba):

        self.bomber = b.bomber
        self.jogador =b.player
        self.setor.extend(b.sectors)
        bombs.remove(b)
       
    def clear_sectors(self, map, b):

        for i in self.setor:
            if  map[i[0]][i[1]] == 2:
                b.bomber.pontos[b.player] +=1
            map[i[0]][i[1]] = 0

    def update(self, dt):
        self.time = self.time - dt