#a5.12.Remove duplicates.
numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print("Original List:", numbers)
print("Without Duplicates:", unique)
