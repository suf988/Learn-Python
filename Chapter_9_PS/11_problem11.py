# Q11: Write a python program to rename a file to “renamed_by_ python.txt.

# IMP_NOTE: in this question, i am not properly renaming a file. I am copying the content of a file and creating a new file with same content.

# However, i could delete the original file with 'os module', i wouldn't do that bcoz at this point of time, I haven't studied the 'os module'

with open("old_file.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

print("Success!!")