import pygame

pygame.init()

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Définir la taille de la fenêtre
taille_fenetre = (1080, 720)
fenetre = pygame.display.set_mode(taille_fenetre)

MOUTON_COUNT = 5




def home_page():
    fond_home = pygame.image.load('image/game.png')
    fond_home = pygame.transform.scale(fond_home ,(1080,720))
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
    fond_settings= pygame.transform.scale(fond_settings ,(1080,720))
    fenetre.blit(fond_settings, (0,0))

    # Définir les dimensions et la position du bouton
    largeur_bouton =  55
    hauteur_bouton = 55
    position_bouton_quit = pygame.Rect(820, 45, largeur_bouton, hauteur_bouton)
    position_bouton_add = pygame.Rect(400, 400, largeur_bouton, hauteur_bouton)
    
    pygame.draw.rect(fenetre, BLANC, position_bouton_quit,1)
    pygame.draw.rect(fenetre, BLANC, position_bouton_add,1)


    # Définir le texte des options
    police = pygame.font.SysFont("Arial", 50)
    texte = police.render(f"{MOUTON_COUNT}", True, NOIR)
    fenetre.blit(texte, (370, 410))

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
                if position_bouton_add.collidepoint(event.pos):
                    MOUTON_COUNT+=1
                    texte = police.render(f"{MOUTON_COUNT}", False, NOIR)
                    print(f"bouton mouton : {MOUTON_COUNT}")
                    
                    pygame.display.flip()
        pygame.display.update()

    home_page()

    


if __name__ == "__main__":
       home_page()



