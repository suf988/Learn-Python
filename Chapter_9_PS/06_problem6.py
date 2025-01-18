# Q6: Write a program to mine a log file and find out whether it contains ‘python’.

with open("log_file.html") as f:
    data = f.read().lower()

    if "python" in data:
        print("Log file contains keyword 'python'")
    else:
        print("Log file does not contain keyword 'python'")
