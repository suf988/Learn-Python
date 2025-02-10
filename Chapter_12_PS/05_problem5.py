# Q5: Store the multiplication tables generated in problem 3 in a file named Tables.txt.

number = int(input("Enter a number: "))

table = [number*i for i in range(1,11)]
print(table)

with open('Tables.txt', 'a') as f:  # opened the file in append mode so that whenever the code runs, the table is appended
    f.write(f"Table of {number}: {str(table)}\n")