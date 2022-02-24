class Car:
    def __init__(self, model, color, owner): # Constructor
        self.model = model # instance attribute
        self.color = color
        self.owner = owner

    def print_car_details(self, num): # Method
        return f'Model: {self.model}, Color: {self.color}, Owner: {self.owner}'    
        
        
car1 = Car('pride', 'blue', 'Elnaz Dehkharghani') # instance
print(car1.owner)
print(car1.print_car_details(20)) 
print(Car.print_car_details(car1, 20)) # Equal to above


