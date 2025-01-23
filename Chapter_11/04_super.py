# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  SUPER METHOD
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
* when a child class inherits its parent class, it has access to all attributes and methods.

* but Constructors (__init__) require explicit calls to the parent using super() if the child defines its own constructor.
'''

# ===================================================================

# If the child class does not define its own __init__, it automatically uses the parent class's constructor.
# For example:

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    age = 24

child = Child("Alice")
print(f"Name: {child.name}")
print(f"Age: {child.age}")

# ===================================================================

# If the parent class has an __init__ constructor, it will not be called automatically when the child class defines its own __init__ constructor. You need to call it explicitly using super().

class Parent2:

    def __init__(self, name):
        self.name = name
        print("Hello from Parent Class\n") 

class Child2(Parent2):

    def __init__(self, name, age):
        super().__init__(name)      # super().__init__() calls the constructor of parent.
        print("Hello from Child Class\n")
        self.age = age
    

child2 = Child2("Harry", 30)
print(f"Name: {child2.name}")
print(f"Age: {child2.age}")