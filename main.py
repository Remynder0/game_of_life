from config import *
from elements import *
from planets import *

print(Ground())
print(Resource("Water","W",10))
a = Animal ( "Dragon", "D",30)
a.ageing()
a.losing_life(10)
a.recovering_life(5)
a.get_ids_counts()
print(a)