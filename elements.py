import random

class Element:

    __ids_counts=0

    @classmethod
    def get_ids_counts(cls):
        return cls.__ids_counts
    def incr_ids_counts(cls):
        cls.__ids_counts+=1

    
    def __init__(self,name,char_repr):
        self.__name=name
        self.__char_repr=char_repr
        self.__id=self.__ids_counts+1
        Element.incr_ids_counts(Element)
        



    def get_name(self):
        return f"{self.__name}"
    
    def get_id(self):
        return self.__id

    def get_char_repr(self):
        return f"{self.__char_repr}"
    
    def __repr__(self) -> str:
        return f"{self.get_char_repr()} : {self.get_name()} n°{self.get_id()}"



class Ground(Element):
    def __init__(self, name="Ground", char_repr="."):
        super().__init__(name, char_repr)


class Resource(Element):
    def __init__(self, name, char_repr):
        super().__init__(name, char_repr)

    def __repr__(self) -> str:
        return f"{super().__repr__()} ({self.get_id()})"


class Herb(Resource):
    def __init__(self, name="Herb", char_repr="\U0001F33F"):
        super().__init__(name, char_repr)

class Water(Resource):
    def __init__(self, name="Water", char_repr="\U0001F41F"):
        super().__init__(name, char_repr,)


class Animal(Element):

    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr)
        self.__life_max=life_max
        self.__age=0
        self.__gender=random.randint(0, 1)
        self.__bar_life=[life_max,life_max]
        self.__current_direction=[random.randint(-1, 1),random.randint(-1, 1)]


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


    ########### direction ############            
    def get_current_direction(self):
        return self.__current_direction
    
    def set_direction(self,line,column):
        self.__current_direction=[line,column]

    ########### représentation ############ 
    def __repr__(self) -> str:
        return f"{super().__repr__()} ({self.get_gender()} de {self.get_age()} an(s))\n - Barre de vie : {self.get_life()}/{self.get_life_max()}"
    

class Mouse(Animal):
    def __init__(self, name="Mouse", char_repr="\U0001F42D", life_max=2):
        super().__init__(name, char_repr, life_max)

class Lion(Animal):
    def __init__(self, name="Lion", char_repr="\U0001F981", life_max=10):
        super().__init__(name, char_repr, life_max)

class Dragon(Animal):
    def __init__(self, name="Dragon", char_repr="\U0001F432", life_max=20):
        super().__init__(name, char_repr, life_max)

class Cow(Animal):
    def __init__(self, name="Cow", char_repr="\U0001F42E", life_max=5):
        super().__init__(name, char_repr, life_max)









class Cow(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Pig(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Sheep(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Bunny(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Fish(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Bear(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Wolf(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Snake(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Falcon(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)