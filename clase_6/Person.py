


class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age



    def ShowInformation(self):
        print(f'name: {self.name} age:{self.age}')



class Employee(Person):
    def __init__(self,name,age,salary,hours):
        super().__init__(name,age)
        self.salary = salary
        self.hours = hours



max = Employee('max',19,2000,8)

max.ShowInformation()