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
        self.__id=int()

    def get_name(self):
        return f"{self.__name}"
    
    def get_id(self):
        return self.__id

    def get_char_repr(self):
        return f"{self.__char_repr}"
    
    def __repr__(self) -> str:
        pass



class Ground(Element):
    def __init__(self, name, char_repr):
        super().__init__(name, char_repr)


class Resource(Element):
    def __init__(self, name, char_repr,value):
        super().__init__(name, char_repr)
        self.__value=value
    
    def get_value(self):
        return self.__value


class Herb(Resource):
    def __init__(self, name, char_repr, value):
        super().__init__(name, char_repr, value)

class Water(Resource):
    def __init__(self, name, char_repr, value):
        super().__init__(name, char_repr, value)


class Animal(Element):

    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr)
        self.__life_max=life_max
        self.__age=int()
        self.__gender=int()
        self.__bar_life=[int(),int()]
        self.__current_direction=[int(),int()]


    ############# age/genre #############
    def get_age(self):
        return self.__age
    
    def ageing(self):
        self.__age+=1

    def get_gender(self):
        return self.__gender
    

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
                self.__bar__life[0]=self.__bar_life[1]
            else:
                self.__bar_life=self.__bar_life+value

    def losing_life(self,value):
        # variable temp
        life=self.get_life()

        if life>0:
            if life<value:
                self.__bar__life[0]=0
            else:
                self.__bar_life=self.__bar_life-value


    ########### direction ############            
    def get_current_direction(self):
        return self.__current_direction
    
    def set_direction(self,line,column):
        self.__current_direction=[line,column]


    def __repr__(self) -> str:
        pass
    

class Mouse(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Lion(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Dragon(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)

class Cow(Animal):
    def __init__(self, name, char_repr, life_max):
        super().__init__(name, char_repr, life_max)