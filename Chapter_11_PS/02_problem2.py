# Q2: Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’

class Animals:
    def __init__(self, animal):
        self.animal = animal

class Pet(Animals):
    pass

class Dog(Pet):
    def bark(self):
        print(f"The {self.animal} makes barking sound.")

dog = Dog("Dog")
dog.bark()