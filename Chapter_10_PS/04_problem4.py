# Q4: Add a static method in problem 2, to greet the user with hello.

class Calculator:

    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"Square of number {self.n} is: {self.n**2}")
    
    def cube(self):
        print(f"Cube of number {self.n} is: {self.n**3}")
    
    def sqrt(self):
        print(f"Square root of number {self.n} is: {self.n ** (1/2)}")
    
    @staticmethod
    def greet():
        print("Hello!")

num = Calculator(16)
num.greet()
num.square()
num.cube()
num.sqrt()