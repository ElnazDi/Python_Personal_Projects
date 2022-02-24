class Person:
    country = 'iran' # class attribute

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def age(self, birth_year):
        return (1401 - birth_year)



class Father(Person):
    def __init__(self, fname, lname, job, wife, children):
        super().__init__(fname, lname) # inheritance from Person  
        self.job = job
        self.wife = wife
        self.children = children

    def introduce(self):
        return f'I am {self.fname} {self.lname}. My wife name is {self.wife} and I have {self.children} children.'


class Child(Father):
    def __init__(self, fname, lname, job, couple_name, children, country):
        super().__init__(fname, lname, job, couple_name, children) 
        self.country = country # If forget to put it, it shows iran

    def introduce(self):
        return f'I am {self.fname} and I live in {self.country}'          



person1 = Person('elnaz', 'dehkharghani')
print(person1.age(1365))  

father1 = Father('Hamidreza', 'Dehkharghani', 'Retired', 'Fariba', 3)
print(father1.introduce())

child1 = Child('Elnaz', 'Dehkharghani','student', 'Hassan', '0', 'Germany')
print(child1.introduce())

help(child1) # shows the order of inheritance

