# Q2: A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

'''
7
14
.
.
.

'''

list_of_seven = [str(i*7) for i in range(1,11)]

vertical = "\n".join(list_of_seven)

print(vertical)