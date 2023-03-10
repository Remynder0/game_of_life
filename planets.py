from grid import Grid

class PlanetAlpha(Grid):

    NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, 1)
    NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (-1, 1), (1, 1),(1, -1),(-1, -1) 
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = (NORTH,NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST,NORTH_WEST)

    def __init__ (self,longitude_cells_count, latitude_cells_count, ground):
        grid_init = [[ground] * longitude_cells_count for _ in range(latitude_cells_count)]
        Grid.__init__(self, grid_init)
        self.__current_animals_count = 0
        self.__ground = ground


    def get_current_animals_count(self):
        pass

    def incr_current_animals_count(self):
        pass

    def decr_current_animals_count(self):
        pass

    def get_ground(self):
        pass

    def is_free_place(self, cell_number):
        pass

    def get_random_free__place(self):
        pass

    def place_resources(self, list):
        pass

    def place_animals(self):
        pass

    def get_grid_char_repr(self):
        pass

    def get_count(self, value):
        pass

    def has_equal_values(self, value):
        pass

    def get_same_value_cell_numbers(self, value):
        pass

    def get_line_str(self, line_number, separator):
        pass

    def draw_with_turtle(self, cell_size, margin, show_values):
        pass











    
