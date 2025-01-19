# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  SELF PARAMETER
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# when we define a method(a function in class), we give it a 'self' parameter.
# it refers to the attributes of class.
# it is necessary to give a self parameter in a method, whether we use it or not. Or else it wil throw an error.

class Employee:
    language = "Python"
    region = "Emilia-Romagna"
    city = "Bologna"

    @staticmethod   # if we dont want to pass self parameter, we mark the method with 'staticmethod' decorator.
    def greet():
        print("Good Morning!")
    
    def getInfo(self):
        print(f"The user '{self.name}' is a {self.language} developer. He lives in {self.city} in {self.region} region.")

harry = Employee()
harry.name = "Harry"
harry.language = "JavaScript"

harry.greet()   
harry.getInfo() # these methods calling are referred as Employee.getInfo(harry)