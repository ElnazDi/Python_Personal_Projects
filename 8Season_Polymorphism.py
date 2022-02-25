class Shape: # Abstract class
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def area(self): 
        '''since we do not know the childs shapes
         in advance we only force them to have area inside them'''
        raise NotImplementedError('All children of the Shape class needs to have area!')


class Circle(Shape): # Child
    pi = 3.14 # class attribute

    def __init__(self, name, r=10): 
        ''' r = 10 you can skip as input since it is here by default'''
        super().__init__('Circle', name) # Inherits
        self.radius = r  # instance attribute

    def area(self): # methode
        return Circle.pi * (self.radius **2)  # if self.pi then changeable (circle1.pi = 3.14444)


class Square(Shape): # Child
    def __init__(self, type ,name, side_length):
        super().__init__(type, name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2    



def calc_area(shape):
    '''change this to function print(square1.area())'''
    print(shape.area())


    

circle1 = Circle('a', 10) # defined type in chiled (better way - compare two classes)
circle2 = Circle('a', 20) 

square1 = Square('Square','a', 10) 
square2 = Square('Square','a', 20) 


# put the shapes in a list
shap_list = [circle1, circle2, square1, square2]

# apply the calc_area() function for all shapes
for shape in shap_list:
    calc_area(shape)

     
