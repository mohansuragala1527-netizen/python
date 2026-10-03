#lab6 task4
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = filter(lambda x: x % 2 == 0, nums)

# Square the even numbers
squares = map(lambda x: x ** 2, evens)

# Add all squares
total = reduce(lambda a, b: a + b, squares)

print("Total using map, filter and reduce:", total)


# Using list comprehension and sum()
total2 = sum(x ** 2 for x in nums if x % 2 == 0)

print("Total using list comprehension:", total2)
