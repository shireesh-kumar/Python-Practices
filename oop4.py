#python encapsulation
#Access Specifier
class Student:
    def __init__(self,marks):
        self.__privateVariableDeclaration = None
        self._totalMarks = marks #conventional way to declare a private variable even though its not completely private as above
    
    def setPrivateVariableValue(self,x):
        __privateVariableDeclaration = 123 * x
        return __privateVariableDeclaration


obj = Student(25)
print(obj.setPrivateVariableValue(1))


