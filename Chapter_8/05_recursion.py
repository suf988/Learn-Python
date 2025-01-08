# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  RECURSION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# recursion are the function that keep calling themselves.
# with the help of recursion, you can solve mathematical formulas in a more direct way.

# FACTORIAL OF A NUMBER:

'''
factorial of 0 = 1
factorial of 1 = 1
factorial of 2 = 2 x 1
factorial of 3 = 3 x 2 x 1
factorial of 4 = 4 x 3 x 2 x 1
factorial of 5 = 5 x 4 x 3 x 2 x 1

factorial of n = n x (n-1) x (n-2) x ............ x 3 x 2 x 1
factorial of n = n x factorial(n-1)

'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"Factorial of number {n} is: {factorial(n)}")

'''
+++++   REASON  +++++

considering n=5

Each time factorial(n) is called, its n value and its "paused" state (waiting for factorial(n-1)) are stored on the stack.

When the base case is reached, the stack starts "unwinding" by returning the results back through the paused calls.

-----------------------------------------------------------------------

Here's what the stack looks like as the program runs:

While Recursing (pushing to stack):

factorial(5)    →   Waiting for factorial(4)
factorial(4)    →   Waiting for factorial(3)
factorial(3)    →   Waiting for factorial(2)
factorial(2)    →   Waiting for factorial(1)
factorial(1)    →   Base case reached!


During Unwinding (popping from stack):

factorial(1)    returns 1   →   factorial(2)    calculates  2 * 1 = 2
factorial(2)    returns 2   →   factorial(3)    calculates  3 * 2 = 6
factorial(3)    returns 6   →   factorial(4)    calculates  4 * 6 = 24
factorial(4)    returns 24  →   factorial(5)    calculates  5 * 24 = 120
'''