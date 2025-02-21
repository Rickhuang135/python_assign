# OOP (object oriented programing)

class programming_lanuage:
    
    def __init__(self, name, binary, package_manager,default_variable_types):
        self.name = name
        self.binary = binary
        self.package_manager = package_manager
        self.default_variable_types = default_variable_types

    def make_variable(self, variable_name, variable_value):
        if type(variable_name).__name__ in self.default_variable_types:
            return f"{variable_name} = {variable_value}"
        else:
            raise Exception("type is not default")

    def output_to_terminal(self):
        return "print"

python = programming_lanuage("python", "python3", "pip", ("str", "int", "float","list","tuple","set","dictionary"))
# python.output_to_terminal()
# print(type(python))
# print(python.make_variable('k',3))


# ***Tutorial Examples
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
    
#     def __repr__(self):
#         return str({"name": self.name, "age": self.age, "grade": self.grade})

#     def get_grade(self):
#         return self.grade
    
    
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = set()

#     def add_student(self, student):
#         if type(student).__name__ != "Student":
#             raise Exception("argument 2 must be of class student")
#         else:
#             if student in self.students or len(self.students) >= self.max_students:
#                 raise Exception("student already in course or course is full")
#             else:
#                 self.students.add(student)

#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)

# compsci130=Course("compsci 130", 3)
# rick=Student("rick", 18, -100)
# compsci130.add_student(rick)
# compsci130.add_student(Student("jim", 18, 200))
# print(compsci130.get_average_grade())
# print(compsci130.students)

# inheretance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am am {self.name}, and I am {self.age} years old")

class Cat(Pet):

    def __init__(self, name, age, width):
        super().__init__(name,age)
        self.width=width

    def speak(self):
        print("meow")

    def show(self):
        print(f"I am am {self.name}, and I am {self.age} years old and {self.width} wide")

class Dog(Pet):
    def speak(self):
        print("bark")

# p = Cat("time", 10 ** 100, 100)
# p.show()


# static class variables and class methods
class Person:
    number_of_people = 0

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


    
# object functions can be replaced, even constructors
# def replace(self, name):
#     self.name =  name
#     print("wow")

# print(Person.number_of_people)
# Person.__init__=replace

# class variables and object variables are different, where object variables can overide class variables
# me = Person("me")
# you = Person("you")
# me.number_of_people=1
# print(me.number_of_people)
# print(you.number_of_people)
# del me.number_of_people
# Person.number_of_people=4
# print(me.number_of_people)
# print(you.number_of_people)

# us = Person("tim")
# them = Person("jill")
# print(Person.number_of_people)


# Static methods
class Math:
    
    @staticmethod
    def add(x,y):
        return x+y

print(Math.add(4,5))


# file handeling 
# file = open("./test.txt","r")
# readfile = file.read()
# print(readfile)
# file.close()

# del readfile

# tkinter
