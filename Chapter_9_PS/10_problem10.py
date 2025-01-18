# Q10: Write a program to wipe out the content of a file using python.

with open("empty_file.html", "w") as f:
    f.write("")
print("Successfully wiped the content of the file.")