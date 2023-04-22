############## importation ###############
import random
import pygame
from elements import *
from config import *
##########################################

class Terrain:

    pygame.init()
    clock = pygame.time.Clock()

    def __init__(self, area_size, background=pygame.image.load('image/fond.png')):
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
            animal_list = pygame.sprite.Group()
            for i in range(ANIMALS_COUNT[key]):
                animal=eval(f"{key}()")
                animal_list.add(animal)
            for sprite in animal_list:
                sprite.rect.x,sprite.rect.y = self.get_random_free_place(sprite)
                x = sprite.rect.x // self.area_size
                y = sprite.rect.y // self.area_size
                self.regions[(x, y)].append(sprite)
        return animal_list
    
    def peacefull_area(self):
        pass
    
    def dangerous_area(self):
        pass

    def affichage(self):
        clock = pygame.time.Clock()
        self.__screen.blit(self.__background, (0,0))

        liste_animals = self.place_animals(ANIMALS_COUNT)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Tester les collisions pour les sprites dans les régions adjacentes
            for sprite in liste_animals:
                sprite.update()
            
                x = sprite.rect.x // self.area_size
                y = sprite.rect.y // self.area_size
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (x+dx, y+dy) in self.regions:
                            for other_sprite in self.regions[(x+dx, y+dy)]:
                                if sprite != other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                    groupe_self = sprite.groups()
                                    print("Collision",groupe_self,"->",other_sprite.groups())

                                    liste_animals.update()


            self.__screen.fill((255, 255, 255))
            self.__screen.blit(self.__background, (0,0))

            for sprite in liste_animals:
                if sprite in liste_animals:
                    self.__screen.blit(sprite.image, (sprite.rect.x,sprite.rect.y))

            pygame.display.flip()
            clock.tick(60)