class Student:
#varname: public
#_varname: protected
#__varname: private
    def __init__(self, name, age, student_id):
        self.__name = name
        self.__age = age
        self.__student_id = student_id

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    
    def __str__(self):
        return f"{self.__name}, {self.__age} years old, ID: {self.__student_id}"