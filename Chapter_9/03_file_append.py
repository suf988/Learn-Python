newString = "\nThis line is appended in the this txt file using the append mode"

f = open("written_file.txt", "a")

f.write(newString)

f.close()