#b3.10.Demonstrate tuple immutability.
numbers = (10, 20, 30)

try:
    numbers[0] = 100
except TypeError as e:
    print("Error:", e)
