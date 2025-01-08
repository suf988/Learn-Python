# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  FUNCTIONS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# functions are seperate piece of logics, that can perform a specified task number of times.
# functions are reuseable.

# FUNCTION DEFINITION:
def func1():
    print("Hello Harry Potter")

# FUNCTION CALL:
func1()     #Hello Harry Potter

# -----------------------------------------------

# printing average of 3 numbers using functions:
def avg():
    a = int(input("Enter 1st number: "))
    c = int(input("Enter 2nd number: "))
    b = int(input("Enter 3rd number: "))

    avg = (a+b+c)/3
    print(f"The average of {a}, {b} and {c} is: {avg:.2f}") # :.2f is used to round off to 2 decimal places
    print(f"The average of {a}, {b} and {c} is: {round(avg,2)}") #round(avg, 2) is also used to round off to 2 dec.

avg()