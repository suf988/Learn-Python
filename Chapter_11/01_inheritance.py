# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  INHERITANCE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Inheritance is a way of creating a new class from an existing class.
# The new class then has all the attributes and methods of its parent class.
# You overwrite or add new methods in the child class.

class Employee:
    company = "Microsoft"

    def __init__(self, name):
        self.name = name

    def getData(self):
        print(f"The employee name is {self.name} and he works in {self.company}")

class Programmer(Employee):  # "Programmer" class inherited the "Employee" class with all its methods and attributes
    company = "Apple"
    language = "Python"

    def getInfo(self):
        print(f"Employee: {self.name}\nCompany: {self.company}\nLanguage: {self.language}")

a = Employee("Harry")
b = Programmer("Hermione")

a.getData()
b.getInfo()