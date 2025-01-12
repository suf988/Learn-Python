# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  APPEND FILE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# append() method is used to append the new text at the end of the file.
# only new data is added to the file, you can not overwrite the existing content of the file.
# will create a new file if the file doesn't exist.

newString = "\nThis line is appended in the this txt file using the append mode"

f = open("written_file.txt", "a")

f.write(newString)

f.close()