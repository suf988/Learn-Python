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

if(chem>=33 and phy>=33 and math>=33 and total_percentage>=40):
    print(f"{stud_name} is passed.")
elif(chem>=33 and phy>=33 and math>=33 and total_percentage<40):
    print(f"{stud_name} is failed as he failed to get atleast 40% overall.")
else:
    failed_str = ", ".join(failed_subs)
    print(f"{stud_name} is failed as he failed to gain atleast 40% in following subjects: {failed_str}")