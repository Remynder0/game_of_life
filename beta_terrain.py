
import random
import pygame
import config
#from beta_menu import *

pygame.init()

ecran = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

clock = pygame.time.Clock()

class MonSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 or self.rect.right > ecran.get_width():
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > ecran.get_height():
            self.vy = -self.vy

    def update_v(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 :
            self.rect.x = ecran.get_width()-self.image.get_width()
        elif self.rect.right > ecran.get_width():
            self.rect.x = 0
        if self.rect.top < 0 :
            self.rect.y = ecran.get_height()-self.image.get_height()
        elif self.rect.bottom > ecran.get_height():
            self.rect.y = 0

    def update_m(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 880 or self.rect.right > ecran.get_width():
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > ecran.get_height():
            self.vy = -self.vy

    def upate_o(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 or self.rect.right > 350:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > 350:
            self.vy = -self.vy

def startGame():
    fond = pygame.image.load('image/fond.png')
    fond = pygame.transform.scale(fond ,(config.WIDTH,config.HEIGHT))
    ecran.blit(fond, (0,0))


    mon_sprite1 = MonSprite(100, 100)
    mon_sprite2 = MonSprite(200, 100)
    mon_sprite3 = MonSprite(200, 300)
    mon_spriteM1 = MonSprite(900, 600)
    mon_spriteM2 = MonSprite(900, 300)
    mon_spriteV1 = MonSprite(820, 0)
    mon_spriteV2 = MonSprite(755, 720)
    mon_spriteV1.vx=0
    mon_spriteV2.vx=0
    mon_spriteO1 = MonSprite(200, 200)

    liste_sprites = [mon_sprite1, mon_sprite2, mon_sprite3]

    liste_spritesV = [mon_spriteV1, mon_spriteV2]
    liste_spritesM = [mon_spriteM1, mon_spriteM2]
    liste_spritesO = [mon_spriteO1]

    # Définir la taille et le nombre de régions
    TAILLE_REGION = 200
    NB_REGIONS_X = ecran.get_width() // TAILLE_REGION
    NB_REGIONS_Y = ecran.get_height() // TAILLE_REGION

    # Initialiser les régions
    regions = {}
    for x in range(NB_REGIONS_X):
        for y in range(NB_REGIONS_Y):
            regions[(x, y)] = []

    # Placer les sprites dans les régions correspondantes
    for sprite in liste_sprites:
        x = sprite.rect.x // TAILLE_REGION
        y = sprite.rect.y // TAILLE_REGION
        regions[(x, y)].append(sprite)
    i=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Tester les collisions pour les sprites dans les régions adjacentes
        
        for sprite in liste_sprites and liste_spritesM:
            if sprite in liste_sprites:
                print('r')
                sprite.update()
            if sprite in liste_spritesM:
                print('v')
                sprite.update_m()
            x = sprite.rect.x // TAILLE_REGION
            y = sprite.rect.y // TAILLE_REGION
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx, y+dy) in regions:
                        for other_sprite in regions[(x+dx, y+dy)]:
                            if sprite != other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                sprite.vx = -sprite.vx
                                sprite.vy = -sprite.vy
                                sprite.rect.x -=5
                                print("Collision r&v:",i)
                                i+=1
                        
        for sprite in liste_spritesV:
            sprite.update_v()
            x = sprite.rect.x // TAILLE_REGION
            y = sprite.rect.y // TAILLE_REGION
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx, y+dy) in regions:
                        for other_sprite in regions[(x+dx, y+dy)]:
                            if sprite!= other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                print("Collision b:",i)
                                i+=1
    
        """for sprite in liste_spritesM:
            sprite.update_m()
            x = sprite.rect.x // TAILLE_REGION
            y = sprite.rect.y // TAILLE_REGION
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx, y+dy) in regions:
                        for other_sprite in regions[(x+dx, y+dy)]:
                            if sprite!= other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                print("Collision v:",i)
                                i+=1"""

        for sprite in liste_spritesO:
            sprite.upate_o()
            x = sprite.rect.x // TAILLE_REGION
            y = sprite.rect.y // TAILLE_REGION
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx, y+dy) in regions:
                        for other_sprite in regions[(x+dx, y+dy)]:
                            if sprite!= other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                print("Collision m:",i)
                                i+=1

        
        
        ecran.fill((255, 255, 255))
        ecran.blit(fond, (0,0))

        #### affichage des sprites ####
        for sprite in liste_sprites:
            pygame.draw.rect(ecran, (255, 0, 0), sprite.rect)
        for sprite in liste_spritesV:
            pygame.draw.rect(ecran, (0, 0, 255), sprite.rect)
        for sprite in liste_spritesM:
            pygame.draw.rect(ecran, (0, 255, 0), sprite.rect)
        for sprite in liste_spritesO:
            pygame.draw.rect(ecran, (164, 82, 33), sprite.rect)
        


        pygame.display.flip()
        clock.tick(60)
    #home_page()





































    
"""
import itertools

# Générer toutes les combinaisons possibles de chiffres entre 0 et 9
combinaisons = itertools.product(range(100), repeat=2)

# Afficher toutes les combinaisons possibles
i=0
for combinaison in combinaisons:
    print(combinaison)
    i+=1

print(i)
"""