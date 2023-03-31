############## importation ###############
import random
import pygame
from elements import *
##########################################

class Terrain:

    def __init__(self, height, weight):
        self.__height = height
        self.__weight = weight

    def is_free_place(self, coordonnee):
        pass
    
    def get_random_free_place(self):
        pass
    
    def place_ressources(self, ressource):
        pass

    def place_animals(self, animals):
        pass
    
    def peacefull_area(self):
        pass
    
    def dangerous_area(self):
        pass