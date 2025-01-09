# Q5: Write a python function to print first n lines of the following pattern:

'''

***
**   for n = 3
*

'''

def pattern(n):
    for i in range(n,0,-1):
        print("*" * i)
        

n = int(input("Enter a number: "))
pattern(n)
# print(printed_pattern)