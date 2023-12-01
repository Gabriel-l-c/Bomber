
import pygame
from typing import Tuple


def load_img(caminho: str, size: Tuple[int, int]):
    image = pygame.image.load(caminho) 
    image = pygame.transform.scale(image, size) 
    image = image.convert_alpha() 
    return image