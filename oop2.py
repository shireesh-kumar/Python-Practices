# functions in a class

class SoftwareEngineer:
    # class  attributes => same copy for all the instances of the class
    alias = "Keyboard Engineer"

    def __init__(self, name, age, city):
        # instance attributes unique for every attribute
        self.name = name
        self.age = age
        self.city = city

    # dunder methods some known functions

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
        # Basically this method can be used to check if two objects are having same values
        # if we dont use this and then write print(ob1, ob 2 ) this it returns false just by comparing their memory locations
        # but if we use this then we compare the values and return the correct result true or false

    def __str__(self):
        # used for the representation of the object when print(obj) is called
        return f"{self.name} leaves in {self.city} city presenttly"

# se1 = SoftwareEngineer("shireesh", 23, "Bangalore")
# se2 = SoftwareEngineer("Shishir", 23, "Dharmasthala")
# se3 = SoftwareEngineer("shireesh", 23, "Bangalore")


# print(se1 == se3 ) #will return false in case if the __eq__ method is not defined


se3 = SoftwareEngineer("shireesh", 23, "Bangalore")
print(se3)
