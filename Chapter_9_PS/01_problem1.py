# Q1: Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

f = open("poems.txt")
data = f.read()
print(f"Text in the file:\n{data}")
data.lower()
if "twinkle" in data:
    print("Text contains 'twinkle' keyword")
else:
    print("Text does not contain 'twinkle' keyword")
f.close()