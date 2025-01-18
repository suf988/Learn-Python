# Q8: Write a program to make a copy of a text file “this. txt”

# reading the content of a file and writing that content in another file created.

with open("poems.txt") as f:
    content = f.read()

with open("this.txt", "w") as f:
    f.write(content)

print("Successfully created a copy file named 'this.txt'")