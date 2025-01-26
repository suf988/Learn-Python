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
value.a = 100   # this will overwrite the class attribue and value of 'a' will be 100 instead of 50.

value.getValue()    #The value of 'a' is 100  //because we modified the class attribue 'a' with instance attribute

# ===================================================================

class Parent2:
    a = 50

    @classmethod
    def getNewValue(cls):
        print(f"Value of 'a' is {cls.a}")

newValue = Parent2()
newValue.a = 100    # tried changing the class attribute with instance attribute.

newValue.getNewValue()  #Value of 'a' is 50  //because the method will only access class attribute due to @classmethod 