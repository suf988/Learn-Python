# Q2: Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

stud_name = input("Enter student's name: ")
chem = int(input("Enter Chemistry marks: "))
phy = int(input("Enter Physics marks: "))
math = int(input("Enter Maths marks: "))

failed_subs = []

if(chem<33):
    failed_subs.append("Chemistry")
if(phy<33):
    failed_subs.append("Physics")
if(math<33):
    failed_subs.append("Maths")

total_percentage = ((chem + phy + math) / 300) * 100

if(total_percentage >= 40 and len(failed_subs) == 0):
    print(f"Congratulations {stud_name}! You've passed the exam")
elif(total_percentage <40):
    print(f"You've failed {stud_name},as total percentage is below 40%")
else:
    failed_subs_str = ",".join(failed_subs)
    print(f"You've failed {stud_name}, because you have less than 30% in following subjects:\n{failed_subs_str}")