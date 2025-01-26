# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  OPERATOR OVERLOADING
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Operators in Python can be overloaded using dunder methods.

# These methods are called when a given operator (such as + - * )is used on the objects.

'''
Operators in Python can be overloaded using the following methods:

p1+p2   =>  p1.__add__(p2)
p1-p2   =>  p1.__sub__(p2)
p1*p2   =>  p1.__mul__(p2)
p1/p2   =>  p1.__truediv__(p2)
p1//p2  =>  p1.__floordiv__(p2)

'''

class Box:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, other):   # dunder method that defines that to do when two objects are added using +
        return f"Sum: {self.num + other.num}"

box1 = Box(12)
box2 = Box(26)

print(box1 + box2)