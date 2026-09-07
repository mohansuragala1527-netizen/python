#a6.19. replace negative number
numbers = [10, -5, 20, -8, 15, -2]

result = [0 if x < 0 else x for x in numbers]

print("Original:", numbers)
print("Result:", result)
