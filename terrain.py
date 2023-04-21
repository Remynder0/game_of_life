############## importation ###############
import random
import pygame
from elements import *
from config import *
##########################################

class Terrain:


    def __init__(self ,background, area_size):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))

        self.area_size = area_size
        NB_REGIONS_X = self.__screen.get_width() // self.area_size
        NB_REGIONS_Y = self.__screen.get_height() // self.area_size
        self.regions = {}
        for x in range(NB_REGIONS_X):
            for y in range(NB_REGIONS_Y):
                self.regions[(x, y)] = []


    def is_free_place(self, x, y, zone):
        rect = pygame.Rect(x, y, zone.rect.width, zone.rect.height)
        return zone.rect.colliderect(rect)
    
    def get_random_free_place(self,surface):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.is_free_place(x,y,surface):
                    return x,y
        return None
    
    def place_ressources(self, ressource):
        for sprite in ressource:
            x = sprite.rect.x // self.area_size
            y = sprite.rect.y // self.area_size
            self.regions[(x, y)].append(sprite)

    def place_animals(self, animals):
        for key in ANIMALS_COUNT.keys():
            animal_list = []
            for i in range(ANIMALS_COUNT[key]):
                animal=f"{key}()"
                animal_list.append(eval(animal))
            for sprite in animal_list:
                sprite.rect.x,sprite.rect.y = self.get_random_free_place(sprite)
                x = sprite.rect.x // self.area_size
                y = sprite.rect.y // self.area_size
                self.regions[(x, y)].append(sprite)
    
    def peacefull_area(self):
        pass
    
    def dangerous_area(self):
        pass