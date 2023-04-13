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
    
    def __init__(self, background = pygame.image.load('image/home.png'), largeur_bouton =  380, hauteur_bouton = 69 ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))
        self.bouton=(largeur_bouton, hauteur_bouton)

    def new_game(self):
        pass
    
    def setting(self):
        print("ok")
        settings=Setting()
    
    def credits(self):
        pass

    def affiche_accueil(self):
        
        self.__screen.blit(self.__background, (0,0))
        position_bouton_settings = pygame.Rect(350, 400-2, self.bouton[0], self.bouton[1])


        RUN=True
        while RUN:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUN = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if position_bouton_settings.collidepoint(event.pos):
                        print("bouton Settings !")
                        RUN = False
                        settings=Setting()
                        settings.affiche_setting()


            pygame.display.update()
    
    



class Setting:
    
    def __init__(self, background = pygame.image.load('image/settings.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))

    def make_button_set(self, id, x, y):
        police = pygame.font.SysFont("Arial", 50)
        intervalle_b=240
        intervalle_nb=120
        position_bouton_addCow = pygame.Rect(x+intervalle_b, y, 30, 50)
        position_bouton_removeCow = pygame.Rect(x, y, 30, 50)
        nb_cow = police.render(f"{id}", True, NOIR)
        self.__screen.blit(nb_cow, (x+intervalle_nb, y+10))

        pygame.draw.rect(self.__screen, BLANC, position_bouton_addCow,1)
        pygame.draw.rect(self.__screen, BLANC, position_bouton_removeCow,1)

    def add(id):
        pass
    def remove(id):
        pass

    def affiche_setting(self):

        self.__screen.blit(self.__background, (0,0))
        position_bouton_quit = pygame.Rect(818, 44, 60, 60)
        self.make_button_set(COW_COUNT,250,193)
        self.make_button_set(SHEEP_COUNT, 250, 399)

        RUN=True
        while RUN:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUN = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if position_bouton_quit.collidepoint(event.pos):
                        print("bouton Quit !")
                        RUN = False
                        game=Home() 
                        game.setting()
                        game.affiche_accueil() 
                    if position_bouton_quit.collidepoint(event.pos):
                        print("bouton Quit !")
                        add(COW_COUNT)      
                        
            pygame.display.update()
   

class Game:
    
    def __init__(self, background = pygame.image.load('image/fond.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))

    def start_game(self):
        pass