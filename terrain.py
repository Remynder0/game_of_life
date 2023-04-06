############## importation ###############
import random
import pygame
from elements import *
from config import *
##########################################

class Terrain:


    def __init__(self ,background):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))

    def is_free_place(self, x, y, zone=pygame.Surface((50, 50))):
        rect = pygame.Rect(x, y, zone.rect.width, zone.rect.height)
        return zone.rect.colliderect(rect)
    
    def get_random_free_place(self,surface):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.is_free_place(x,y,surface):
                    return x,y
        return None
    
    def place_ressources(self, ressource):
        pass

    def place_animals(self, animals):
        pass
    
    def peacefull_area(self):
        pass
    
    def dangerous_area(self):
        pass