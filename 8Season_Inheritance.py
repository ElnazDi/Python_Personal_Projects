class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def intruduce(self):
        return 'This is ' + self.fname.upper() + ' ' + self.lname.upper()


class Student(Person):
    def __init__(self, fname, lname, major, university):
        super().__init__(fname, lname)
        self.major = major
        self.university = university

    def intruduce(self):
        # return super().intruduce() # This is ELNAZ DEHKHARGHANI
        return f'This is {self.fname} {self.lname} , I am studing {self.major} at {self.university}'


class Teacher(Person):
    def __init__(self, fname, lname, department, university):
        super().__init__(fname, lname)
        self.department = department
        self. university = university 

    def intruduce(self):
        return f'I am {self.lname} and I teach in {self.university} in the {self.department} department'







student1 = Student('Elnaz', 'Dehkharghani', 'Data Science', 'SRH')
print(student1.intruduce()) # This is Elnaz Dehkharghani , I am studing Data Science at SRH

teacher1 = Teacher('Frank', 'Schulz', 'Media', 'SRH')
print(teacher1.fname) # Frank
print(teacher1.intruduce()) # I am Schulz and I teach in SRH in the Media department
