# Q1: Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Two_D_Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2D vector has values: {self.i} and {self.j}")

class Three_D_Vector(Two_D_Vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"The 3D vector has values: {self.i}, {self.j} and {self.k}")

a = Two_D_Vector(3,7)
a.show()

b = Three_D_Vector(9,11,15)
b.show()