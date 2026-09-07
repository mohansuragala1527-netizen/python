#a5.11.Demonstrate list methods.
numbers = [30, 10, 20]

numbers.append(40)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.extend([50, 60])
print("After extend:", numbers)

numbers.remove(15)
print("After remove:", numbers)

removed = numbers.pop()
print("Popped element:", removed)
print("After pop:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Count of 30:", numbers.count(30))
print("Index of 30:", numbers.index(30))
