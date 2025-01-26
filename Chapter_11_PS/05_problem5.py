# Q5: Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)