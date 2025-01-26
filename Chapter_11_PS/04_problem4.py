# Q4: Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    def __init__(self, salary, increment):
        self._salary = salary
        self._increment = increment

    @property
    def salary(self):
        return self._salary + (self._salary * self._increment)/100

    @salary.setter
    def salary(self, new_salary):
        self._increment = ((new_salary - self._salary) / self._salary) * 100

sal = Employee(5000, 30)
print(f"Salary after increment: {sal.salary}")

sal.salary = 6500
print(f"Increment: {sal._increment:.0f}%")
