#lab4 task4
numbers = [1, 2, 3, 4, 5, 6, 9]

# Cubes using map()
cubes = list(map(lambda x: x ** 3, numbers))

# Numbers divisible by 3 using filter()
divisible = list(filter(lambda x: x % 3 == 0, numbers))

print("Cubes:", cubes)
print("Numbers divisible by 3:", divisible)
