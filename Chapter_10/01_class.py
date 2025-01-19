# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  OBJECT ORIENTED PROGRAMMING OOP
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# solving the problem by creating objects is one of the most famous approaches in programming.
# The concept focuses on DRY principle (Donot Repeat Yourself) - using reusable code

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  CLASS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
 class is the blueprint to create an object.

 it has all the necessary templates/info to create an object.

 e.g: an empty form has placeholder/template/info that should be filled to complete the form such as name, age, address etc   that empty form is a class
'''

class Employee:         # classes are defined using Pascal case
    language = "py"     # both of these are class attributes
    salary = 85000

harry = Employee()  # object initiation (without initiation, the class is just a template and no memory is assigned)
harry.name = "Harry"
print(f"Name: {harry.name}")    # this is an instance attribute
print(f"Language: {harry.language}")
print(f"Salary: {harry.salary}")

hermione = Employee()
hermione.name = "Hermione"
print(f"Name: {hermione.name}")
print(f"Language: {hermione.language}")
print(f"Salary: {hermione.salary}")

# in the above 2 objects:
'''
"name" is instance attribute because it directly belongs to the object and is different for every object.

"language" and "salary" are class attributes because they directly belong to class and can be same for every object.

e.g: "name" can be different for each user but there can be a class of same "language" and "salary"
'''