# Q3: Check the type of variable assigned using input () function.

variable = input("Enter any data: ")
print("The type of the variable entered is: ", type(variable))  #this will always return str datatype bcoz it is default.

#for specific datatypes, we need to do typecasting.

strVariable = (input("Enter any data: "))
intVariable = int(input("Enter any data: "))
floatVariable = float(input("Enter any data: "))

print(f"Type of 1st variable is {type(strVariable)}")
print(f"Type of 3rd variable is {type(intVariable)}")
print(f"Type of 2nd variable is {type(floatVariable)}")