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
        terrain = Terrain(120)
        return terrain
    
    def setting(self):
        setting = Setting()
        return setting
    
    def credits(self):
        pass

    def affiche_accueil(self):
        
        self.__screen.blit(self.__background, (0,0))
        bouton_settings = pygame.Rect(350, 400-2, self.bouton[0], self.bouton[1])
        bouton_newgame = pygame.Rect(350, 300-2, self.bouton[0], self.bouton[1])



        RUN=True
        while RUN:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUN = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if bouton_settings.collidepoint(event.pos):
                        print("bouton Settings !")
                        RUN = False
                        settings=Setting()
                        settings.affiche_setting()
                    if bouton_newgame.collidepoint(event.pos):
                        print("bouton New Game !")
                        RUN = False
                        new_game=self.new_game()
                        new_game.affichage()

            pygame.display.update()
    
    



class Setting:
    
    def __init__(self, background = pygame.image.load('image/settings.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))
        self.__animal_count = ANIMALS_COUNT

    def add(self, animal):
        self.__animal_count[animal]+=1
    def remove(self, animal):
        if self.__animal_count[animal]>0:
            self.__animal_count[animal]-=1

    def make_button_set(self, id, x, y):
        police = pygame.font.SysFont("Arial", 50)
        intervalle_b=240
        intervalle_nb=120
        bouton_add = pygame.Rect(x+intervalle_b, y, 30, 50)
        bouton_remove = pygame.Rect(x, y, 30, 50)
        nb_cow = police.render(f"{id}", True, NOIR)
        self.__screen.blit(nb_cow, (x+intervalle_nb, y+10))

        pygame.draw.rect(self.__screen, BLANC, bouton_add,1)
        pygame.draw.rect(self.__screen, BLANC, bouton_remove,1)

        return bouton_add, bouton_remove #renvoie les boutons


    def affiche_setting(self):

        self.__screen.blit(self.__background, (0,0))
        bouton_quit = pygame.Rect(818, 44, 60, 60)
        bouton_cow = self.make_button_set(self.__animal_count["Cow"],250,193)
        #bouton_sheep =self.make_button_set(SHEEP_COUNT, 250, 399)

        RUN=True
        while RUN:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUN = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if bouton_quit.collidepoint(event.pos):
                        print("bouton Quit !")
                        RUN = False
                        game=Home() 
                        game.setting()
                        game.affiche_accueil() 
                    if bouton_cow[0].collidepoint(event.pos): #detection du bouton cow 0 (le bouton add)
                        print("bouton cow add")
                        self.add("Cow")    
                        print(self.__animal_count["Cow"])
            pygame.display.update()
   

class Game:
    
    def __init__(self, background = pygame.image.load('image/fond.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))

    def start_game(self):
        pass






"""

j'ai modifié 2-3 trucs pour avoir accés au bouton que l'on crée et aussi la manière que l'on accede au nombre d'animaux
j'ai ajouter un peux de commentaire pour les modifications

(tu peux lancer le fichier beta_menu.py pour voir a quoi resemble ce qu'on a fais)



Voici un petit memo pour les taches que tu as :

# 1. finir les methodes pour ajouter et enlever un animal (l'affichage surtout)
# 2. ajouter aussi une methode pour acceder au nombre d'animaux (regarde dans elements.py il ya une methode "get" quelque chose )
# 3. faire la class methode credits (il y a une fonction credits dans beta_menu.py)
# 4. finir les detection de collision des boutons
# 5. Et surtout n'hésite pas a me demander si tu as un probleme que tu n'arrive pas a resoudre ou que tu comprends pas un trucs

bon coding =)

"""