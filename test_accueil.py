import pygame
import config

pygame.init()

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
MARRON = (164, 82, 33)

# Définir la taille de la fenêtre
WIDTH= config.WIDTH; HEIGHT= config.HEIGHT
taille_fenetre = (WIDTH, HEIGHT)
fenetre = pygame.display.set_mode(taille_fenetre)




def home_page():
    fond_home = pygame.image.load('image/accueil.png')
    fond_home = pygame.transform.scale(fond_home ,(WIDTH,HEIGHT))
    fenetre.blit(fond_home, (0,0))

    # Définir les dimensions et la position du bouton
    largeur_bouton =  380
    hauteur_bouton = 69
    position_bouton_NewGame = pygame.Rect(350, 300-2, largeur_bouton, hauteur_bouton)
    position_bouton_settings = pygame.Rect(350, 400-2, largeur_bouton, hauteur_bouton)
    position_bouton_credits = pygame.Rect(350, 500-2, largeur_bouton, hauteur_bouton)
    position_bouton_quit = pygame.Rect(350, 600-2, largeur_bouton, hauteur_bouton)

    # Dessiner le bouton
    pygame.draw.rect(fenetre, BLANC, position_bouton_NewGame,1)
    pygame.draw.rect(fenetre, BLANC, position_bouton_settings,1)

    RUN=True
    while RUN:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUN = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Vérifier si le clic est dans le bouton
                if position_bouton_NewGame.collidepoint(event.pos):
                    print("bouton New Game !")
                if position_bouton_settings.collidepoint(event.pos):
                    print("bouton Settings !")
                    RUN = False
                    setting_page()
                if position_bouton_credits.collidepoint(event.pos):
                    print("bouton Credits !")
                if position_bouton_quit.collidepoint(event.pos):
                    print("bouton Quit !")
                    RUN = False

        pygame.display.update()


def setting_page():
    print("ok")
    fond_settings = pygame.image.load('image/settings.png')
    fond_settings= pygame.transform.scale(fond_settings ,(WIDTH,HEIGHT))
    fenetre.blit(fond_settings, (0,0))

    # Définir les dimensions et la position du bouton
    position_bouton_quit = pygame.Rect(818, 44, 60, 60)
    position_bouton_addSheep = pygame.Rect(490, 399, 30, 50)
    position_bouton_addCow = pygame.Rect(490, 193, 30, 50)
    
    pygame.draw.rect(fenetre, BLANC, position_bouton_quit,1)
    pygame.draw.rect(fenetre, BLANC, position_bouton_addSheep,1)
    pygame.draw.rect(fenetre, BLANC, position_bouton_addCow,1)



    # Définir le texte des options
    police = pygame.font.SysFont("Arial", 50)
    nb_sheep = police.render(f"{config.SHEEP_COUNT}", True, NOIR)
    fenetre.blit(nb_sheep, (370, 410))
    nb_cow = police.render(f"{config.COW_COUNT}", True, NOIR)
    fenetre.blit(nb_cow, (370, 203))

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
                if position_bouton_addSheep.collidepoint(event.pos):
                    config.SHEEP_COUNT+=1
                    pygame.draw.rect(fenetre, MARRON, pygame.Rect(350, 405, 70, 40))
                    pygame.display.flip()
                    nb_sheep = police.render(f"{config.SHEEP_COUNT}", True, NOIR)
                    fenetre.blit(nb_sheep, (370, 410))
                    #print(f"bouton mouton : {config.SHEEP_COUNT}")
                if position_bouton_addCow.collidepoint(event.pos):
                    config.COW_COUNT+=1
                    pygame.draw.rect(fenetre, MARRON, pygame.Rect(350, 198, 70, 40))
                    pygame.display.flip()
                    nb_cow = police.render(f"{config.COW_COUNT}", True, NOIR)
                    fenetre.blit(nb_cow, (370, 203))
                    #print(f"bouton mouton : {config.COW_COUNT}")
                    
                    
        pygame.display.update()

    home_page()
    return config.SHEEP_COUNT

    


if __name__ == "__main__":
       home_page()



