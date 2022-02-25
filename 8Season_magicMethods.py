class Square:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return f'This is {self.type} with the name of {self.name}' 

    def __len__(self):
         return 8   

    def __del__(self):
        print(f'The {self.name} has been deleted!')      

    

square1 = Square('square', 'a')
print(square1) 
# without __str__ ==> <__main__.Square object at 0x7f9a5c9e9d90>
# with __str__    ==> This is a with the name of square

print(len(square1))
# without __len__ ==> TypeError: object of type 'Square' has no len()
# with __len__    ==> 8

del square1 # The square has been deleted!
# print(square1)




