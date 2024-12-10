# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  TAKING INPUTS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

a = input("Enter first number: ")
b = input("Enter second number: ")
c = a+b
print("Sum of two numbers is: ",c)  #the answer won't be a sum, but both the inputs will be concatenated.
#REASON: the 'input' key will treat both the inputs as string. 
# and the '+' symbol concatenates the strings.

inp1 = int(input("Enter first number: "))   #typecasting of the input as 'int'
inp2 = int(input("Enter second number: "))
result = inp1 + inp2
print("The sum of two numbers is: ", result)