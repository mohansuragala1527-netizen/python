#lab6 task3
from functools import reduce

numbers = [2, 4, 6, 8]

# Product
product = reduce(lambda a, b: a * b, numbers)

# Maximum without max()
maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Product:", product)
print("Maximum:", maximum)


# Concatenate strings
words = ["Python", "is", "easy", "to", "learn"]

sentence = reduce(lambda a, b: a + " " + b, words)

print("Sentence:", sentence)
