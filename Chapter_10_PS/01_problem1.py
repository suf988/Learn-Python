# Q1: Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    residence = "USA"

    def __init__(self, name, exp, salary):
        self.name = name
        self.exp = exp
        self.salary = salary

har = Programmer("Harry", 7, 10000)
her = Programmer("Hermione", 7, 10000)
ron = Programmer("Ron", 5, 7000)
gin = Programmer("Ginny", 3, 5000)

print(f"Name: {har.name}, City: {har.residence}, Company: {har.company}, Experience: {har.exp} yrs, Salary: ${har.salary}")
print(f"Name: {her.name}, City: {her.residence}, Company: {her.company}, Experience: {her.exp} yrs, Salary: ${her.salary}")
print(f"Name: {ron.name}, City: {ron.residence}, Company: {ron.company}, Experience: {ron.exp} yrs, Salary: ${ron.salary}")
print(f"Name: {gin.name}, City: {gin.residence}, Company: {gin.company}, Experience: {gin.exp} yrs, Salary: ${gin.salary}")