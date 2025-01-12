# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  UPDATE FILE (r+)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# used to read and update an existing file.
# will throw an error if the file doesn't exist.
# can update the file, but all the content of the file is not deleted when you open it to update.
# can not add new content at the end, because it will be appending then.

f = open("written_file.txt", "r+")

f.write("This line is written using update mode (r+) ")

f.close()