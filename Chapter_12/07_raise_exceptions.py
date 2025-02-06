# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  RAISE EXCEPTIONS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# "raise" keyword is often used to manually trigger an exception when an error is occured.
# it causes the program to crash.

def age_check(age):
    if age < 18:
        raise ValueError("Age must be older than 18")
    else:
        return "Access granted"

print(age_check(20))    # Access granted
print(age_check(17))    # ValueError: Age must be older than 18

# =========================================================

# another example:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b == 0:
    raise ZeroDivisionError("Divisor can't be zero")
else:
    print(f"{a}/{b} = {a/b:.2f}")


# the error raised in the above mentioned code can be handled more gracefully using try-except.

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num2 == 0:
        raise ZeroDivisionError("Divisor can't be zero!")   # manually raising an error
    else:
        print(f"{num1}/{num2} = {num1/num2:.2f}")
        
except ZeroDivisionError as e:  # catching the manually raised error
    print(f"Error! {e}")        # displaying the error message