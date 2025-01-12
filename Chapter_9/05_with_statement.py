# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  WITH STATEMENT
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# with statement can automatically opens and closes a file.

f = open("file.txt")

data = f.read()
print(data)
f.close()

# the above mentioned file reading code can also be written as below:

with open("file.txt") as f:
    text = f.read()
    print(text)

# you don't have to explicitely close the file.