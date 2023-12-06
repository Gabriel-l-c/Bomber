import pygame
import pygame_menu
import time

from mapa import Mapa
from jogo import Jogo
COLOR_BACKGROUND = (0, 153, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (102, 102, 153)
MENU_TITLE_COLOR = (51, 51, 255)
WINDOW_SCALE = 0.75
# iniciar o dispaly
pygame.display.init()

INFO = pygame.display.Info()

TILE_SIZE = int(INFO.current_h*0.035)

WINDOW_SIZE = (13 * TILE_SIZE, 13 * TILE_SIZE)

clock = None
surface = pygame.display.set_mode(WINDOW_SIZE)

def run_game1():
    Jogo(surface, TILE_SIZE, 1)
    
def run_game2():
    Jogo(surface, TILE_SIZE, 2)
    
def main_background():
    global surface
    surface.fill(COLOR_BACKGROUND)


def menu_loop():
    pygame.init()

    pygame.display.set_caption('Bomberman')
    clock = pygame.time.Clock()

    menu_theme = pygame_menu.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.7),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR,

    )

    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        title='Play menu'
    )
    play_menu.add.button('Start', run_game1)
    
    about_menu_theme = pygame_menu.themes.Theme(
        selection_color=COLOR_WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE*0.5),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITLE_COLOR
    )

#menu principal de escolha de 1 ou 2 personagem / sair
    main_menu = pygame_menu.Menu(
        theme= menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        onclose=pygame_menu.events.EXIT,
        title='Main menu'
    )

    main_menu.add.button('1 Jogador', run_game1)
    main_menu.add.button('2 Jogadores', run_game2)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    running = True
    di = time.time()
#loop de atualização dos"frames do jodo"
    while running:
        
        df = time.time()
        clock.tick(FPS)
        temp_jogo = pygame.time.get_ticks()
        
        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background)

        pygame.display.flip()
        
        if df-di == 1000:
            running = False
            exit()

    exit()


if __name__ == "__main__":
    menu_loop()