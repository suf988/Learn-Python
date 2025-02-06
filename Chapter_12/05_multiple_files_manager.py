# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  MANAGE MULTIPLE CONTEXT FILES
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# You can now use multiple context managers in a single with statement more cleanly using the parenthesised context manager.

with(
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    data1 = f1.read()
    data2 = f2.read()

print(f"Data 1: {data1}")
print(f"Data 2: {data2}")