# Q4: What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))   #length = 2 (bcoz 20 and 20.0 would be same so only one value will be added to the set)