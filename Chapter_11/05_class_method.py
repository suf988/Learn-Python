# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  CLASS METHOD
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a "class method" is a method that bounds the method to use the attribute of the class, not the instance.
# it is initialized by putting a "class method" decorator on a method.

class Parent:
    a = 50

    def getValue(self):
        print(f"The value of 'a' is: {self.a}")

value = Parent()
value.a = 100

value.getValue()