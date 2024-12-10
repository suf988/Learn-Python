# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  TAKING INPUTS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

a = input("Enter first number: ")
b = input("Enter second number: ")
c = a+b
print("Sum of two numbers is: ",c)  #the answer won't be a sum, but both the inputs will be concatenated.
#REASON: the 'input' key will treat both the inputs as string. 
# and the '+' symbol concatenates the strings.