# if an attribute is already defined inside a class, and it is changed during assignment as instance attribute:
# instance attribute will be prefered over class attribute.

class Employee:
    language = "Python"
    city = "Milan"

harry = Employee()
harry.language = "JavaScript"   # this instance attribute will be preferred over class attribute of language
print(f"Language: {harry.language}")
print(f"City: {harry.city}")