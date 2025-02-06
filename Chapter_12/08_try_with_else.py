# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  TRY STATEMENT WITH ELSE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# the 'else' block only runs in a try-except structure if no exception occurs inside the 'try' block.
# it makes the code more cleaner and readable by seperating the normal execution from the error handling try-catch

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a/b

except ZeroDivisionError as e:
    print(e)

else:
    print(f"Result: {result:.2f}")