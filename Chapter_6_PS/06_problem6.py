# Q6: Write a program to calculate the grade of a student from his marks from the following scheme:

# 90 – 100 => Ex
# 80 – 89 => A
# 70 – 79 => B
# 60 – 69 =>C
# 50 – 59 => D
# <50 => F

marks = int(input("Enter your total marks: "))

if(marks>=90 and marks<=100):
    print("Your grade: EX")
elif(marks>=80 and marks<90):
    print("Your grade: A")
elif(marks>=70 and marks<80):
    print("Your grade: B")
elif(marks>=60 and marks<70):
    print("Your grade: C")
elif(marks>=50 and marks<60):
    print("Your grade: D")
elif(marks<50):
    print("Your grade: F")