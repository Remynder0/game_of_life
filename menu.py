############## importation ###############
import random
import pygame
from elements import *
from terrain import *
from config import *
import config
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
    
    def credit(self):
        credit = Credit()
        return credit

    def affiche_accueil(self):
        
        self.__screen.blit(self.__background, (0,0))
        bouton_newgame = pygame.Rect(350, 300-2, self.bouton[0], self.bouton[1])
        bouton_settings = pygame.Rect(350, 400-2, self.bouton[0], self.bouton[1])
        bouton_credits = pygame.Rect(350, 500-2, self.bouton[0], self.bouton[1])
        
        
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

                    if bouton_credits.collidepoint(event.pos):
                        print("bouton credits !")
                        RUN = False
                        crediit = Credit()
                        crediit.affiche_credits()

            pygame.display.update()
    
    



class Setting:
    
    def __init__(self, background = pygame.image.load('image/settings.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))
        self.__element_count = DEFAULT_COUNT
        

    def get_nb_count(self,element):
        return self.__element_count[element]

    def add(self, element):
        if self.__element_count[element] > 0 and self.__element_count[element]< self.get_nb_count(element):
            self.__element_count[element]+=1

    def remove(self, element):
        if self.__element_count[element] > 0:
            self.__element_count[element]-=1

    def make_button_set(self, id, x, y):
        police = pygame.font.SysFont("Arial", 45)
        intervalle_b=240
        intervalle_nb=120
        bouton_add = pygame.Rect(x+intervalle_b, y, 30, 50)
        bouton_remove = pygame.Rect(x, y, 30, 50)
        nb_cow = police.render(f"{id}", True, NOIR)
        txt_rect = nb_cow.get_rect()
        txt_rect.centerx = (bouton_add.left + bouton_remove.right)//2
        txt_rect.centery = (bouton_add.top + bouton_remove.bottom)//2
        self.__screen.blit(nb_cow, txt_rect)


        pygame.draw.rect(self.__screen, BLANC, bouton_add,1)
        pygame.draw.rect(self.__screen, BLANC, bouton_remove,1)

        return bouton_add, bouton_remove #renvoie les boutons


    def affiche_setting(self):
        police = pygame.font.SysFont("Arial", 45)
        self.__screen.blit(self.__background, (0,0))
        bouton_quit = pygame.Rect(818, 44, 60, 60)
        
        
        bouton_cow = self.make_button_set(self.__element_count["Cow"],250,196)
        bouton_pig = self.make_button_set(self.__element_count["Pig"], 250, 300)
        bouton_sheep = self.make_button_set(self.__element_count["Sheep"], 250, 402)
        bouton_rabbit = self.make_button_set(self.__element_count["Rabbit"], 250, 510)

        bouton_falcon = self.make_button_set(self.__element_count["Falcon"], 556, 196)
        bouton_snake = self.make_button_set(self.__element_count["Snake"], 556, 300)
        bouton_wolf = self.make_button_set(self.__element_count["Wolf"], 556, 402)
        bouton_fish = self.make_button_set(self.__element_count["Fish"], 556, 510)

        """boutons = {
            (bouton_cow[0], "cow", "add"),
            (bouton_pig[0], "pig", "add"),
            (bouton_sheep[0], "sheep", "add"),
            (bouton_rabbit[0], "cow", "add"),
            (bouton_falcon[0], "cow", "add"),
            (bouton_snake[0], "cow", "add"),
            (bouton_wolf[0], "cow", "add"),
            (bouton_fish[0], "cow""add")
        }
        """

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
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 198, 80, 41))
                        pygame.display.flip()
                        nb_cow = police.render(f"{self.__element_count['Cow']}", True, NOIR)
                        self.__screen.blit(nb_cow, (370, 200))

                    if bouton_cow[1].collidepoint(event.pos):
                            print("bouton cow remove")
                            self.remove("Cow")
                            pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 198, 80, 41))
                            pygame.display.flip()
                            nb_cow = police.render(f"{self.__element_count['Cow']}", True, NOIR)
                            self.__screen.blit(nb_cow, (370, 200))
                                
                    if bouton_pig[0].collidepoint(event.pos):
                        print("bouton pig add")
                        self.add("Pig")
                        print(self.__element_count["Pig"])
                    if bouton_sheep[0].collidepoint(event.pos):
                        print("bouton sheep add")
                        self.add("Sheep")
                        print(self.__element_count["Sheep"])
                    if bouton_rabbit[0].collidepoint(event.pos):
                        print("bouton rabbit add")
                        self.add("Rabbit")
                        print(self.__element_count["Rabbit"])
                    if bouton_falcon[0].collidepoint(event.pos):
                        print("bouton falcon add")
                        self.add("Falcon")
                        print(self.__element_count["Falcon"])
                    if bouton_snake[0].collidepoint(event.pos):
                        print("bouton snake add")
                        self.add("Snake")
                        print(self.__element_count["Snake"])
                    if bouton_wolf[0].collidepoint(event.pos):
                        print("bouton wolf add")
                        self.add("Wolf")
                        print(self.__element_count["Wolf"])
                    if bouton_fish[0].collidepoint(event.pos):
                        print("bouton fish add")
                        self.add("Fish")
                        print(self.__element_count["Fish"])

                    """
                    if action == "add" : 
                        print("bouton fish add")
                        self.add(element)
                        print(self.__element_count[element])
                    """    


            pygame.display.update()
   


class Credit:

    def __init__(self, background = pygame.image.load('image/credits.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))
    
    def affiche_credits(self):
        police = pygame.font.SysFont("Arial", 32)
        self.__screen.blit(self.__background, (0,0))
        position_bouton_quit = pygame.Rect(726, 140, 60, 60)
        pygame.draw.rect(self.__screen, BLANC, position_bouton_quit,1)


        music_source1 = police.render("Subwoofer Lullaby by C418", True, NOIR)
        music_source2 = police.render("From Minecraft-Volume Alpha n°03", True, NOIR)
        self.__screen.blit(music_source1, (355,460))
        self.__screen.blit(music_source2, (355,490))

        author1 = police.render("Tom", True, NOIR)
        author2 = police.render("Eliott", True, NOIR)
        author3 = police.render("Remy", True, NOIR)
        author4 = police.render("Kheda", True, NOIR)
        self.__screen.blit(author1, (355,295))
        self.__screen.blit(author2, (355,325))
        self.__screen.blit(author3, (355,355))
        self.__screen.blit(author4, (355,385))
        pygame.display.flip()

    
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
                        game.credit()
                        game.affiche_accueil() 
                        
            pygame.display.update()

    #home_page()






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

# 1. finir les methodes pour ajouter et enlever un element (l'affichage surtout)
# 2. ajouter aussi une methode pour acceder au nombre d'animaux (regarde dans elements.py il ya une methode "get" quelque chose )
# 3. faire la class methode credits (il y a une fonction credits dans beta_menu.py)
# 4. finir les detection de collision des boutons
# 5. Et surtout n'hésite pas a me demander si tu as un probleme que tu n'arrive pas a resoudre ou que tu comprends pas un trucs

bon coding =)

"""