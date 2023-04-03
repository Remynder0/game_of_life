############## importation ###############
import random
import pygame
from elements import *
from terrain import *
from config import *
##########################################

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
MARRON = (164, 82, 33)



class Home:

    pygame.init()
    
    def __init__(self, background = pygame.image.load('image/accueil.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))


    def affiche_accueil(self):
        
        self.__screen.blit(self.__background, (0,0))

        RUN=True
        while RUN:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUN = False

            pygame.display.update()
    
    def new_game(self, config):
        pass
    
    def setting(self):
        pass
    
    def credits(self):
        pass



class Setting:
    
    def __init__(self, background = pygame.image.load('image/settings.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))

    def get_setting(self):
        pass

    def affiche_setting(self):
        pass

class Game:
    
    def __init__(self, background = pygame.image.load('image/fond.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))

    def start_game(self):
        pass