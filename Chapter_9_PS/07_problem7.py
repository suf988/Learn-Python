# Q7: Write a program to find out the line number where python is present from ques 6.

line = 1

# Method 1:     Using readline()

with open("log_file.html") as f:
    data = f.readline()
    if 'python' in data:
        print(f"Keyword 'python' is present in line no. {line}")
    else:    
        line += 1
        while(data != ""):
            if 'python' in data:
                print(f"Keyword 'python' is present in line no. {line}")
                break
            line += 1
            data = f.readline()
        else:
            print("Keyword 'python' is not present.")


# =================================================================

# Method 2:     Using readlines()

with open("log_file.html") as f:
    data = f.readlines()

    for i in data:
        if 'python' in i:
            print(f"Keyword 'python' is present in line no. {line}")
            break
        line += 1
    else:
        print("Keyword 'python' is not present.")
    