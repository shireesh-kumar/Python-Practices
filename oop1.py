#Functions in classes


class SoftwareEngineer:
    # class  attributes => same copy for all the instances of the class
    alias = "Keyboard Engineer"

    def __init__(self, name, age, city):
        # instance attributes unique for every attribute
        self.name = name
        self.age = age
        self.city = city

    # instance methods
    def printAge(self):
        print(f"Age of {self.name} is {self.age}")

    # parameterized function
    def codeLanguage(self, language):
        print(f"{self.name} is writing code in {language} language ")

    def salary(age):
        if(age > 25):
            print("Salary : 23445 ")
        else:
            print("Salary : 13245")

    @staticmethod
    def salary1(age):
        if(age > 25):
            print("Salary : 23445 ")
        else:
            print("Salary : 13245")


# Creating a instance of a class
se1 = SoftwareEngineer("shireesh", 23, "Bangalore")

# print("Name : {} , City : {} , Age : {} ".format(se1.name, se1.city, se1.age))


# Calling the instance methods of the class
# se1.printAge()
# se1.codeLanguage("Python")


# What is i dont want the obj instance method call not to pass self
# Type1 calling using the class name
SoftwareEngineer.salary(23)
# or use a decorator @staticmethod
se1.salary1(30)
