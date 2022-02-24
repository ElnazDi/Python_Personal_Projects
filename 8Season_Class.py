class House:
    country = 'iran' # class attribute

    def __init__(self, color, rooms, area):
        self.color = color # instance attribute
        self.rooms = rooms
        self.area = area

    def print_details(self): # class method
        return(self.color, self.rooms, self.area)


elnaz_home = House('blue', 4, 120)


elnaz_home.country = 'USA'
print(elnaz_home.country) # USA
del elnaz_home.country   # remove USA
print(elnaz_home.country) # iran : Back to its first version








