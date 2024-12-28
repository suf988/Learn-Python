# Q2: Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
marks.append(int(input("Enter marks of 1st student: ")))
marks.append(int(input("Enter marks of 2nd student: ")))
marks.append(int(input("Enter marks of 3rd student: ")))
marks.append(int(input("Enter marks of 4th student: ")))
marks.append(int(input("Enter marks of 5th student: ")))
marks.append(int(input("Enter marks of 6th student: ")))
marks.append(int(input("Enter marks of 7th student: ")))

print(f"Marks of students (unsorted): {marks}")
marks.sort()
print(f"Marks of students (sorted): {marks}")