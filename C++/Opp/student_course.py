class Student:

    def __init__(self,name,lastName,courses):
        self.name = name
        self.lastName = lastName
        self.courses = courses


    def show_courses(self):
        for course in self.courses:
            print(course)



class Course:
    


max = Student("max","mora",[1,2,3,4,5])
max.show_courses()