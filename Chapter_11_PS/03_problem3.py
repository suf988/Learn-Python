# Q3: Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:
    def __init__(self, salary):
        self.salary = salary
    
    def increment(self, increment):
        self.salary += increment
        return f"Original Salary: {self.salary}\nSalary after increment of {increment}: {self.salary}"

sal = Employee(5000)
print(sal.increment(3000))