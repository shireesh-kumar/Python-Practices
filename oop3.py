# inheritance

class Employee:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def details(self):
        print(f"{self.name} is from {self.city} city")

#inheritance , extends , override


class SoftwareEngineer(Employee):  # inheritance
    def __init__(self, name, city, age, salary):
        super().__init__(name, city)
        self.age = age
        self.salary = salary

    def printSalary(self):
        print(self.salary)  # extended functionality

    def details(self):  # override
        print(f"{self.name} is working")


obj1 = SoftwareEngineer("Shireesh", "Bangalore", 23, 34000)
# obj1.details()


class Designer(Employee):
    def __init__(self, name, city, srn):
        super().__init__(name, city)
        self.srn = srn

    def details(self):
        print(f"{self.name} is designing")


# Polymorphism
# Now we have two classes inheriting same Employee class

employees = [SoftwareEngineer("Shishir", "Dharmasthala", 23, 34000), Designer(
    "Vatsa", "Bangalore", "R16CS")]


def get_details(emps):
    for i in emps:
        i.details()


get_details(employees)  # appropriate details method will be called wrt class
