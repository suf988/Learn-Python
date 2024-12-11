# Q2: Write a program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Imran").replace("<|Date|>", "12-11-2024"))