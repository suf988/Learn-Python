# Q1: Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

try:

    with open('one.txt') as one:
        print(one.read())
        
except Exception as e:
    print(e)

try:

    with open('two.txt') as two:
        print(two.read())

except Exception as e:
    print(e)
try:

    with open('three.txt') as three:
        print(three.read())

except Exception as e:
    print(e)