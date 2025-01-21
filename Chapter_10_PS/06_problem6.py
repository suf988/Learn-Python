# Q6: Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

# Yes, we can change the self-parameter inside a class to something else. Because it is just a parameter afterall.
# But, if the parameter is changed to something else instead to 'self', that word should replace 'self' everywhere.

# Example:
class Employee:
    category = "Programmers"
    language = "Python"
    salary = 1500
    location = "USA"

    def __init__(slf, name, experience):
        slf.name = name
        slf.experience = experience 

    def completeInfo(slf):
        print(f"Name: {slf.name}\nEmployee category: {slf.category}\nLanguage: {slf.language}\nLocation: {slf.location}\nsalary: ${slf.salary * slf.experience}")
    

adam = Employee("Adam", 7)
adam.completeInfo()