
import random
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

if __name__ == "__main__" :
    random.seed (1000)
    planet = PlanetAlpha ( "Terre" , PLANET_LONGITUDE_CELLS_COUNT, PLANET_LATITUDE_CELLS_COUNT, Ground () )
    planet.place_resources([ Herb () for _ in range (HERBS_COUNT) ] )
    planet.place_resources([ Water () for _ in range (WATERS_COUNT) ] )
    planet.place_animals([ Lion () for _ in range (LIONS_COUNT) ] )
    planet.place_animals([ Dragon () for _ in range (DRAGONS_COUNT) ] )
    planet.place_animals([Cow() for _ in range (COWS_COUNT) ] )
    planet.place_animals([ Mouse () for _ in range (MOUSES_COUNT) ] )
    print ( planet.get_grid_str ( ) )
    h , w, l , d , c , m, g = Herb () , Water () , Lion () , Dragon () , Cow() , Mouse () , Ground ()
    print ( f"La planète {planet.get_name()} a {planet.get_lines_count() * planet.get_column_count()} places" , end=" ")
    print ( f"avec {planet.get_current_animals_count()} animaux qui s’y baladent: ")
    for element in (h , w, l , d , c , m, g ) :
        print ( f"\t {planet.get_count(element)} {element.get_name()} : {planet.get_same_value_cell_numbers(element)}")
    dragon_cell_number = planet.get_same_value_cell_numbers(d)[0]
    line_dragon , column_dragon = planet.get_coordinates_from_cell_number ( dragon_cell_number )
    print(f"\t Le voisinage de {d.get_char_repr()} aux points cardinaux est :" , end=" ")
    print([element.get_char_repr()
        for element in planet.get_neighborhood(line_dragon , column_dragon , planet.CARDINAL_POINTS, True )])
    print(f"\t Le voisinage complet de {d.get_char_repr()} est : " , end=" ")
    print([element.get_char_repr()
        for element in planet.get_neighborhood (line_dragon , column_dragon , planet .WIND_ROSE, True )])
    planet.draw_with_turtle(PLANET_CELL_PIXEL_SIZE)