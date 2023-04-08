
import random
import pygame
import config

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

def startGame():
    mon_sprite1 = MonSprite(100, 100)
    mon_sprite2 = MonSprite(200, 100)
    mon_sprite3 = MonSprite(200, 300)
    liste_sprites = [mon_sprite1, mon_sprite2, mon_sprite3]

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Tester les collisions pour les sprites dans les régions adjacentes
        for sprite in liste_sprites:
            sprite.update()
            x = sprite.rect.x // TAILLE_REGION
            y = sprite.rect.y // TAILLE_REGION
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx, y+dy) in regions:
                        for other_sprite in regions[(x+dx, y+dy)]:
                            if sprite != other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                print("Collision !")
                            else:
                                print("RAS")
        ecran.fill((0, 0, 0))
        for sprite in liste_sprites:
            pygame.draw.rect(ecran, (255, 0, 0), sprite.rect)
        pygame.display.flip()
        clock.tick(60)






































    
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