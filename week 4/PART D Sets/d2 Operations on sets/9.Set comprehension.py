#d2.9.Set comprehension
squares = {x ** 2 for x in range(1, 21) if x % 2 != 0}

print("Squares of Odd Numbers:", squares)
