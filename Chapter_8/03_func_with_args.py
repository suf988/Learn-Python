# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  FUNCTIONS WITH ARGUMENTS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a function can accept some values when it is called and those values can be used or executed inside the function.

def func1(name, greeting):  #this function is taking to arguments and using them inside the function.
    print(f"{greeting} {name}, how are you today?")

func1("Harry", "Good morning")  #Good morning Harry, how are you today?
func1("Sara", "Good evening")   #Good evening Sara, how are you today?
func1("Hermione", "Hello")      #Hello Hermione, how are you today?

print("\n=================================================\n")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  FUNCTIONS WITH RETURN
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# we can use "return" statement inside a function to return a value from a function.
# that value can be assigned to a vairable and can be reused anywhere further if needed in the program.

def func2(num1, num2):
    average = (num1 + num2)/2
    return average

a = func2(23, 56)
b = func2(69, 87)

print(f"The first average of two numbers is: {a:.2f}")
print(f"The second average of two numbers is: {b:.2f}")
print(f"The sum of the two averages is: {a+b}")