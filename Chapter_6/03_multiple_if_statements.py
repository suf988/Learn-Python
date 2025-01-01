# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  MULTIPLE IF STATEMENTS 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
age = int(input("Enter your age: "))

# if-statements can work independently.
# so, if there are multiple if-statements, all shall run and shall run independently.


# start of if-statement 1
if(age%2==0):
    print("Age is even number")
# end of if-statement 1


# start of if-statement 2
if(age<=0):
    print("Invalid age! Please enter a valid age")
elif(age>=18):
    print("You are above 18! You are good to go")
else:
    print("Sorry! You are below 18")
# end of if-statement 2
