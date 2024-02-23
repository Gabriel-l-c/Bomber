
import sys
import pygame

from map import Map
from pacman import Pacman


def main():
    SCREEN_HEIGHT = 300
    SCREEN_WIDTH = 600
    TILE_SIZE = 30
    PACMAN_SIZE = 20

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    map_rows = SCREEN_HEIGHT // TILE_SIZE
    map_cols = SCREEN_WIDTH // TILE_SIZE
    map = Map(map_cols, map_rows)

    pacman = Pacman(map, PACMAN_SIZE, TILE_SIZE)

    while True:
        events = pygame.event.get()
        
        for event in events:
            if (event.type == pygame.QUIT) or (pygame.key.get_pressed()[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit(0)
        
        pacman.handle_events()
        
        screen.fill((255, 255, 255))
        map.draw(screen, tile_size=TILE_SIZE)
        pacman.draw(screen)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()