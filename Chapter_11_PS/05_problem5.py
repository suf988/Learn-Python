# Q5: Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        real_part = self.r * other.r - self.i * other.i
        imaginary_part = self.r * other.i + self.i * other.r
        return Complex(real_part, imaginary_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i" 
    
    def __str(self):
        return f"{self.r} * {self.i}i"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(f"Sum of two complex numbers: {c1 + c2}")
print(f"Product of two complex numbers: {c1 * c2}")