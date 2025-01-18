# Q3: Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

def multiply():
    for i in range(2,21):
        with open(f"tables/table of {i}", 'w') as f:

            f.write(f"Table of {i}\n")
            for j in range(1,11):
                f.write(f"\n{i} x {j} = {i*j}")
    print("Successfully stored multiplication tables of 2-20 in different seperate files")

multiply()