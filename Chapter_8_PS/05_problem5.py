# Q5: Write a python function to print first n lines of the following pattern:

'''

***
**   for n = 3
*

'''
# USING FOR LOOP:

def pattern(n):
    for i in range(n,0,-1):
        print("*" * i)
        
# USING RECURSION:
def pattern_rec(n):
    if n==0:
        return
    print("*"*n)
    pattern_rec(n-1)

n = int(input("Enter a number: "))
print("\nUSING FOR LOOP:\n")
pattern(n)
print("\nUSING RECURSION:\n")
pattern_rec(n)