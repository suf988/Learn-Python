# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  FILTER FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# The filter() function is used to filter elements from an iterable based on a condition. It returns a new iterable containing only the elements that satisfy the condition.

# SYNTAX: filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# another example:  (filtering short words)
words = ["apple", "banana", "kiwi", "mango", "strawberry"]

long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)

# another example:  (filtering negative numbers)
nums = [-10, 15, -20, 30, -5, 40]

positive_num = list(filter(lambda x: x > 0, nums))
print(positive_num)

# another example:  (filtering vowels from string)
inp = input("Enter words: ")
vowels = 'aeiou'

filter_vowels = list(filter(lambda x: x in vowels, inp))
print(filter_vowels)