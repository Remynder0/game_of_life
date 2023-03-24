class Home:
    
    def __init__(self, largeur, longueur):
        self.screen = (largeur, longueur)
        self.font = Font()
        self.bouton = None

    def affiche_accueil(self):
        pass
    
    def new_game(self, config):
        pass
    
    def setting(self):
        pass
    
    def credits(self):
        pass



class Setting:
    
    def __init__(self, largeur, longueur, config):
        self.__config = config
        self.screen = (largeur, longueur)
        self.font = Font()
        self.bouton = None

    def get_setting(self):
        pass

    def affiche_setting(self):
        pass

class Game:
    
    def __init__(self, largeur, longueur):
        self.screen = (largeur, longueur)
        self.font = Font()
        self.bouton = None

    def start_game(self):
        pass