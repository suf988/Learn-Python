# Q7: Write __str__() method to print the vector as follows:

#  7i + 8j +10k 

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v1 = Vector(3,4,5)
v2 = Vector(6,7,8)

print(v1 + v2)