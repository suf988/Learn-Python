# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  PROPERTY DECORATOR
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# consider the following code: (without property decorator)

class Employee:
    def __init__(self, salary):
        self.salary = salary
    
    def get_salary(self):
        return f"Salary: {self.salary}"
    
    def set_salary(self, value):
        if value < 0:
            raise ValueError("Invalid input! Salary can't be negative.")
        self.salary = value

emp = Employee(5000)
print(emp.get_salary()) # method had to be called to get the value

emp.set_salary(10000)   # method had to be called to set the value
print(emp.get_salary())

