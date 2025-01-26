# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  PROPERTY DECORATOR
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Example without property decorator
class Employee:
    def __init__(self, salary):
        self.salary = salary
    
    def get_salary(self):  # Getter method to retrieve salary
        return f"Salary: {self.salary}"
    
    def set_salary(self, value):  # Setter method to modify salary
        if value < 0:
            raise ValueError("Invalid input! Salary can't be negative.")
        self.salary = value

emp = Employee(5000)
print(emp.get_salary())  # Method explicitly called to get the salary

emp.set_salary(10000)   # Method explicitly called to set the salary
print(emp.get_salary())

'''
The above code works, but explicitly calling getter and setter methods is less clean and makes the code less readable.

We can use @property decorators to make the code cleaner, allowing attribute-style access for getting and setting values.
'''

# Example with @property decorator
class Employee2:
    def __init__(self, salary):
        self._salary = salary  # Internal attribute for storing salary
    
    @property  # Getter method to retrieve salary
    def salary(self):
        return f"Salary: {self._salary}"
    
    @salary.setter  # Setter method to modify salary
    def salary(self, value):
        if value < 0:
            raise ValueError("Invalid input! Salary can't be negative.")
        self._salary = value

emp2 = Employee2(15000)
print(emp2.salary)  # Accessing the salary like an attribute

emp2.salary = 20000  # Setting salary like an attribute
print(emp2.salary)