# Q2: Write a class “Calculator” capable of finding square, cube and square root of a number.

import math

class Calculator:

    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"Square of number {self.n} is: {self.n**2}")
    
    def cube(self):
        print(f"Cube of number {self.n} is: {self.n**3}")
    
    def sqrt(self):
        print(f"Square root of number {self.n} is: {math.sqrt(self.n)}")

num = Calculator(16)
num.square()
num.cube()
num.sqrt()