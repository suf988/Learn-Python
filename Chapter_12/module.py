# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  if __name__ == "__main__"
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Every Python script has a built-in variable called __name__.

# When a script is run directly, __name__ is set to "__main__".
# When a script is imported as a module, __name__ is set to the script’s filename (without .py).

def add(a,b):
    return a + b

if __name__ == "__main__":
    print(f"Code executed from '{__name__}'")
    x = 8
    y = 32
    print(f"Sum: {add(x, y)}")