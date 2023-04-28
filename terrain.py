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
    
    def get_random_place(self,zone):
        x= random.randint(0,WIDTH)
        y=random.randint(0,HEIGHT)
        return x,y                  

    
    def create_groups(self):
        #creation des different groupes de elements
        peacefull_list = pygame.sprite.Group()
        savaged_list = pygame.sprite.Group()
        car_list = pygame.sprite.Group()
        human_list = pygame.sprite.Group()
        resource_list = pygame.sprite.Group()
        print(ELEMENTS_COUNT.keys())
        for key in ELEMENTS_COUNT.keys():
            for i in range(ELEMENTS_COUNT[key]):
                element=eval(f"{key}()")
                if element.type == "peacefull":
                    for i in range(ELEMENTS_COUNT[key]):
                        peacefull_list.add(element)
                elif element.type == "savaged":
                    for i in range(ELEMENTS_COUNT[key]):
                        savaged_list.add(element)
                elif element.type == "car":
                    for i in range(ELEMENTS_COUNT[key]):
                        car_list.add(element)
                elif element.type == "resource":
                    for i in range(ELEMENTS_COUNT[key]):
                        resource_list.add(element)
                elif element.type == "human":
                    for i in range(ELEMENTS_COUNT[key]):
                        human_list.add(element)

        return peacefull_list, savaged_list, car_list, human_list
        
    
    def place_elements(self, elements_list):

        for sprite in elements_list:
            sprite.rect.x,sprite.rect.y = self.get_random_place([0,500])
            print(sprite.rect.x,sprite.rect.y)
            x = sprite.rect.x // self.area_size
            y = sprite.rect.y // self.area_size
            self.regions[(x, y)].append(sprite)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 or self.rect.right > self.__screen.get_width():
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > self.__screen.get_height():
            self.vy = -self.vy
    
    def peacefull_area(self):
        pass
    
    def dangerous_area(self):
        pass

    def affichage(self):
        clock = pygame.time.Clock()
        self.__screen.blit(self.__background, (0,0))

        liste_elements = self.create_groups()
        liste_animals = liste_elements[0]
        self.place_elements(liste_animals)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            self.__screen.blit(self.__background, (0,0))

            # Tester les collisions pour les sprites dans les régions adjacentes
            for sprite in liste_animals:
                sprite.update()
                self.__screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
            
                x = sprite.rect.x // self.area_size
                y = sprite.rect.y // self.area_size
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (x+dx, y+dy) in self.regions:
                            for other_sprite in self.regions[(x+dx, y+dy)]:
                                if sprite != other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                    groupe_self = sprite.groups()
                                    #print("Collision",groupe_self,"->",other_sprite.groups())

                                    liste_animals.update()

            

            

            pygame.display.flip()
            clock.tick(60)