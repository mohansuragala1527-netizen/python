#lab4 task1
# Square of a number
square = lambda x: x * x
# Check even or odd
even = lambda x: "Even" if x % 2 == 0 else "Odd"
# Find larger of two numbers
larger = lambda a, b: a if a > b else b
print("Square:", square(5))
print("Check:", even(3))
print("Larger:", larger(5, 10))
