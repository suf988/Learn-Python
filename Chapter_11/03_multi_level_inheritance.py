# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  MULTI LEVEL INHERITANCE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# here, a class which is child itself, becomes parent for its child class

#   PARENT =>   CHILD =>    CHILD

class Animal:
    adjective = "cute"

    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.adjective} {self.name} makes a sound.")

class Mammal(Animal):
    
    def sound(self):
        print(f"{self.name} is a {self.adjective} mammal and makes a specific sound.")

class Dog(Mammal):
    pass
    def sound(self):
        print(f"{self.adjective} {self.name} barks.")

dog = Dog("Buddy")

dog.sound()

# When you call dog.sound(), Python first looks for the sound method in the Dog class. Since it finds it there, it executes that version of the method.

# If the Dog class didn’t define a sound method, it would fall back to the Mammal class, and then to the Animal class if necessary.