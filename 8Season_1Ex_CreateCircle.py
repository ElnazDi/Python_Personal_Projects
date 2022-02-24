class Circle:
    pi = 3.14 # class attribute

    def __init__(self, r): # constructur
        self.r = r  # instance attribute

    def cal_diameter(self): # instance methos
        return self.r * 2    

    def cal_circumference(self):
        # return 2 * self.pi * self.r   # use self.pi -> check in instance -> changeable
        # return 2 * Circle.pi * self.r  # use Circle.pi -> check in Class -> Not changeable

    def cal_area(self):
        # return self.pi * (self.r **2)
        # return Circle.pi * (self.r **2)


circle1 = Circle(5)

print(circle1.cal_diameter())
print(circle1.cal_area()) # 78.5 Circle.pi | 78.5 self.pi
print(circle1.cal_circumference()) 

circle1.pi = 2.4
print(circle1.cal_area()) # 78.5 Circle.pi | 60.0 self.pi
