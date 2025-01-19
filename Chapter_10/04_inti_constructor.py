# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  __INIT__() CONSTRUCTOR
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# __init__() constructor is a special method that runs automatically as soon as the object is initiated.
# it takes 'self' arguement and can take other arguements as well.

class Employee:
    language = "Python"
    salary = 80000
    city = "Bologna"

    def __init__(self, name, salary, language): # these methods are also called dunder methods (starting with __ )
        print("The object is created and the __init__ method is called automatically")
        self.name = name
        self.salary = salary
        self.language = language

harry = Employee("Harry", 10000, "JavaScript")  
# harry.name = "Harry"
# harry.language = "JavaScript"

print(f"Name: {harry.name}")
print(f"Language: {harry.language}")
print(f"Salary: {harry.salary}")
print(f"City: {harry.city}")