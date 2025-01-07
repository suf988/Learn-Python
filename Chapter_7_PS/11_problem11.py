# Q10: Write a program to print the following star pattern.
'''
*************
 ***********
  *********
   *******    
    *****
     ***    for n = 7
      *
     ***
    *****
   *******
  *********
 ***********
*************

'''

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1))

for j in range(2, n+1):
    print(" "*(n-j), end="")
    print("*"*(2*j-1))