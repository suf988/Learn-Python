# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  GLOBAL KEYWORD
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# A global variable can be used anywhere in the script.

a = 100  # Global variable

def func():
    print(a)

func()

# ------------------------------------------------------

# If there is a local variable inside a function, that function will refer to the local variable instead of the global one.

b = 100  # Global variable

def func2():
    b = 50  # Local variable (only accessible inside this function)
    print(b)

print(b)  # Outputs: 100 (global variable)
func2()   # Outputs: 50 (local variable inside func2)

# ------------------------------------------------------

# To modify a global variable inside a function, we use the 'global' keyword.

c = 200  # Global variable

def func3():
    global c  # Declaring 'c' as global to modify it
    c = 500   # Changing the global variable
    print(c)

func3()  # Outputs: 500
