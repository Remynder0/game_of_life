#### importation ######
import random
import pygame

class Element(pygame.sprite.Sprite):

    __ids_counts=0

    @classmethod
    def get_ids_counts(cls):
        return cls.__ids_counts
    def incr_ids_counts(cls):
        cls.__ids_counts+=1

    
    def __init__(self,name):
        super.__init__()
        self.name=name
        self.rect = self.image.get_rect()
        self.__id=self.__ids_counts+1
        Element.incr_ids_counts(Element)
        
    def get_id(self):
        return self.__id
   


class Resource(Element):
   def __init__(self,durability,name):
        super.__init__(name)
        self.__durability=durability

class Stone(Resource):
    def __init__(self,name="Stone",durability=10):
        super.__init__(durability,name)
        self.__image = pygame.image.load("image/stone.png").convert_alpha()
        
class Plant(Resource):
    def __init__(self,name="Plant", durability=2):
        super.__init__(durability,name) 
        self.__image = pygame.image.load("image/plant.png").convert_alpha()

class Iron(Resource):
    def __init__(self,name="Iron",durability=12):
        super.__init__(durability)
        self.__image = pygame.image.load("image/stone.png").convert_alpha()

class Three(Resource):
    def __init__(self,name="Iron", durability=6):
        super.__init__(durability) 
        self.__image = pygame.image.load("image/three.png").convert_alpha()


class Animal(Element):

    def __init__(self,life_max,name):
        super.__init__(name)
        self.__life_max=life_max
        self.__age=0
        self.__gender=random.randint(0, 1)
        self.__bar_life=[life_max,life_max]


    ############# age/genre #############
    def get_age(self):
        return self.__age
    
    def ageing(self):
        self.__age+=1

    def get_gender(self):
        if self.__gender:
            return "mâle"
        else:   
            return "femelle"
    

    ############# point de vie ###############
    def get_life_max(self):
        return self.__life_max
 
    def get_life(self):
        return self.__bar_life[0]
    
    def is_alive(self):
        if self.get_life(): return True
            
        else: return False
            
    def is_dead(self):
        if self.get_life(): return False
            
        else: return True
            
    def recovering_life(self,value):
        # variables temp
        life=self.get_life()
        life_max=self.get_life_max()

        if life<life_max:
            if life_max-life<value:
                self.__bar_life[0]=life_max
            else:
                self.__bar_life[0]=life+value

    def losing_life(self,value):
        # variable temp
        life=self.get_life()

        if life>0:
            if life<value:
                self.__bar_life[0]=0
            else:
                self.__bar_life[0]=life-value


    ########### mouvement ############            
    def movement():
        pass
    


class Cow(Animal):
    def __init__(self, name="Cow", life_max=10):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/cow.png").convert_alpha()


class Pig(Animal):
    def __init__(self, name="Pig", life_max=8):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/pig.png").convert_alpha()


class Sheep(Animal):
    def __init__(self, name="Sheep", life_max=8):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/sheep.png").convert_alpha()


class Rabbit(Animal):
    def __init__(self, name="Bunny", life_max=1):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/rabbit.png").convert_alpha()

class Fish(Animal):
    __poisson=('Basile','Emile')
    def __init__(self, name="Fish", life_max=1):
        super().__init__(name, life_max)
        self.__image = pygame.image.load(f"image/fish{self.__poisson[random.randint(0, 1)]}.png").convert_alpha()


class Bear(Animal):
    def __init__(self, name="Bear", life_max=30):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/bear.png").convert_alpha()

class Wolf(Animal):
    def __init__(self, name="Wolf", life_max=15):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/wolf.png").convert_alpha()

class Snake(Animal):
    def __init__(self, name="Snake", life_max=2):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/snake.png").convert_alpha()

    def poisoned():
        pass


class Car(Animal):
    def __init__(self, name="Car", life_max=100):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/car.png").convert_alpha()


class Falcon(Animal):
    def __init__(self, name="Falcon", life_max=2):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/falcon.png").convert_alpha()


class Human(Animal):
    def __init__(self, name="Human", life_max=10):
        super().__init__(name, life_max)
        self.__image = pygame.image.load("image/gru.png").convert_alpha()
        self.__inventory = []
        self.arms=0
        self.tools=0

        
    def crafting():
        pygame.time.Clock()

