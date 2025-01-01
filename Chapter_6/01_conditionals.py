age = int(input("Enter your age: "))

if(age<=0):
    print("Invalid age! Please enter a valid age")
elif(age>=18):
    print("You are above 18! You are good to go")
else:
    print("Sorry! You are below 18")