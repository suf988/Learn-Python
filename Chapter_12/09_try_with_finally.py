# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  TRY STATEMENT WITH FINALLY
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# the "finally" block in try-catch structure always executes no matter an exception happens or not!
# it is usually used for clean-up operations like closing the files, releasing resources.
# it is also used in functions even after a return statement.

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a/b
    print(f"Result: {result:.2f}")

except ZeroDivisionError as e:
    print(e)

finally:
    print("Execution completed!")

# =============================================

# another example:

def main():
    try:

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        return  a/b

    except ZeroDivisionError as e:
        return f"Invalid operation! {e}"

    finally:
        print("Execution completed!")   # this finally block will still execute even after return statement

print(main())